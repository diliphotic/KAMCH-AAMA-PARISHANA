from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone
import secrets

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Security
security = HTTPBasic()

ADMIN_USERNAME = "admin_kamch"
ADMIN_PASSWORD = "adminkamch123"

# Define Models
class PatientAssessment(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    age: str
    gender: str
    date: str
    mobile: str
    
    # Assessment responses (1-5 scale)
    q1_aruchi: int  # Reduced appetite
    q2_gaurava: int  # Heaviness
    q3_chhardi: int  # Nausea
    q4_rasa_vaishamya: int  # Altered taste
    q5_alasya: int  # Laziness
    q6_shirashoola: int  # Headache
    q7_prishta_kati: int  # Backache
    q8_trishna: int  # Thirst
    q9_malavastambha: int  # Constipation
    q10_mala_dourghandhyata: int  # Foul smelling stools
    q11_mala_chikkanata: int  # Sticky stools
    q12_mala_pravritti: int  # Bowel frequency
    q13_daurbalya: int  # Weakness
    q14_lack_enthusiasm: int  # Lack of enthusiasm
    
    total_score: int
    result: str  # "Ama not present" / "Ama slightly present" / "Ama Present"
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class PatientAssessmentCreate(BaseModel):
    name: str
    age: str
    gender: str
    date: str
    mobile: str
    
    q1_aruchi: int
    q2_gaurava: int
    q3_chhardi: int
    q4_rasa_vaishamya: int
    q5_alasya: int
    q6_shirashoola: int
    q7_prishta_kati: int
    q8_trishna: int
    q9_malavastambha: int
    q10_mala_dourghandhyata: int
    q11_mala_chikkanata: int
    q12_mala_pravritti: int
    q13_daurbalya: int
    q14_lack_enthusiasm: int

class AdminLogin(BaseModel):
    username: str
    password: str

class AdminLoginResponse(BaseModel):
    success: bool
    message: str

# Helper function to calculate result
def calculate_assessment_result(data: PatientAssessmentCreate) -> tuple[int, str]:
    total_score = (
        data.q1_aruchi + data.q2_gaurava + data.q3_chhardi + 
        data.q4_rasa_vaishamya + data.q5_alasya + data.q6_shirashoola +
        data.q7_prishta_kati + data.q8_trishna + data.q9_malavastambha +
        data.q10_mala_dourghandhyata + data.q11_mala_chikkanata + 
        data.q12_mala_pravritti + data.q13_daurbalya + data.q14_lack_enthusiasm
    )
    
    # Score-based result calculation
    if total_score >= 43:
        result = "Ama Present"
    elif total_score >= 29:
        result = "Ama slightly present"
    else:
        result = "Ama not present"
    
    return total_score, result

# Routes
@api_router.get("/")
async def root():
    return {"message": "Kamch Aam Parikshan API"}

@api_router.post("/assessment", response_model=PatientAssessment)
async def submit_assessment(input: PatientAssessmentCreate):
    # Calculate result
    total_score, result = calculate_assessment_result(input)
    
    # Create assessment object
    assessment_dict = input.model_dump()
    assessment_dict['total_score'] = total_score
    assessment_dict['result'] = result
    assessment_obj = PatientAssessment(**assessment_dict)
    
    # Convert to dict and serialize datetime to ISO string for MongoDB
    doc = assessment_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    # Save to database
    await db.assessments.insert_one(doc)
    
    return assessment_obj

@api_router.post("/admin/login", response_model=AdminLoginResponse)
async def admin_login(credentials: AdminLogin):
    if credentials.username == ADMIN_USERNAME and credentials.password == ADMIN_PASSWORD:
        return AdminLoginResponse(success=True, message="Login successful")
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@api_router.get("/admin/assessments", response_model=List[PatientAssessment])
async def get_all_assessments():
    # Fetch all assessments from database
    assessments = await db.assessments.find({}, {"_id": 0}).to_list(10000)
    
    # Convert ISO string timestamps back to datetime objects
    for assessment in assessments:
        if isinstance(assessment['timestamp'], str):
            assessment['timestamp'] = datetime.fromisoformat(assessment['timestamp'])
    
    # Sort by timestamp descending (newest first)
    assessments.sort(key=lambda x: x['timestamp'], reverse=True)
    
    return assessments

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
