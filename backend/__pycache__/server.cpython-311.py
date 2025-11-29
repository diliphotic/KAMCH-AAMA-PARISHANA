§
    •{)i»  ã                   ót  — d dl mZmZmZmZ d dlmZm Z  d dlm	Z	 d dl
m
Z
 d dlm
Z
 d dlZd dlZd d lmZ d dlmZmZmZ d d	lmZmZ d dlZd d
lmZmZ d dlZ ee¦  «        j        Z e	ed
z
  ¦  «         ej         d         Z! e
e!¦  «        Z"e"ej         d
                  Z# e¦   «         Z$ ed¬¦  «        Z% e¦   «         Z&dZ'dZ( G d„ de¦  «        Z) G d„ de¦  «        Z* G d„ de¦  «        Z+ G d„ de¦  «        Z,de*de-e.e/f         fd„Z0e% 1                    d¦  «        d„ ¦   «         Z2e% 3                    de)¬ ¦  «        d!e*fd"„¦   «         Z4e% 3                    d#e,¬ ¦  «        d$e+fd%„¦   «         Z5e% 1                    d&ee)         ¬ ¦  «        d'„ ¦   «         Z6e$ 7                    e%¦  «         e$ 8                    e
d(ej          1                    d)d*¦  «         9                    d+¦  «        d*gd*g¬,¦  «          ej:        ej;        d-¬.¦  «          ej<        e=¦  «        Z>e$ ?                    d/¦  «        d0„ ¦   «         Z@dS )1é    )Ú FastAPIÚ	APIRouterÚ
HTTPExceptionÚ Depends)Ú	HTTPBasicÚHTTPBasicCredentials)Ú
load_dotenv)ÚCORSMiddleware)ÚAsyncIOMotorClientN)ÚPath)Ú	BaseModelÚFieldÚ
ConfigDict)ÚListÚOptional)ÚdatetimeÚtimezonez.envÚ	MONGO_URLÚ DB_NAMEz/api)ÚprefixÚ
admin_kamchÚ
adminkamch123c                   óB  — e Zd ZU  ed¬¦  «        Z ed„ ¬¦  «        Ze ed<   e ed<   e ed <   e ed<   e ed	<   e ed
<   e	ed
<   e	ed<   e	ed
<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e	ed<   e ed<    ed„ ¬¦  «        Z
e
ed<   dS )ÚPatientAssessmentÚignore)Úextrac                  óB   — t          t          j        ¦   «         ¦  «        S ©N)ÚstrÚuuidÚuuid4© ó    ú/app/backend/server.pyú<lambda>zPatientAssessment.<lambda>'   s   € ­Cµ´
±´Ñ,=Ô,=€ r#   )Údefault_factoryÚidÚnameÚageÚgenderÚdateÚmobileÚ	q1_aruchiÚ
q2_gauravaÚ
q3_chhardiÚq4_rasa_vaishamyaÚ	q5_alasyaÚq6_shirashoolaÚq7_prishta_katiÚ
q8_trishnaÚq9_malavastambhaÚq10_mala_dourghandhyataÚq11_mala_chikkanataÚq12_mala_pravrittiÚ
q13_daurbalyaÚq14_lack_enthusiasmÚ
total_scoreÚresultc                  ó>   — t          j        t          j        ¦  «        S r   )r   Únowr   Úutcr"   r#   r$   r%   zPatientAssessment.<lambda>@   s   € ½¼ÅXÄ\Ñ8RÔ8R€ r#   Ú	timestampN)Ú__name__Ú
__module__Ú__qualname__r   Úmodel_configr   r'   r   Ú__annotations__Úintr@   r   r"   r#   r$   r   r   $   sC  € € € € € € Ø: HÐ-Ñ-Ô-€LàˆeÐ$=Ð$=Ð>Ñ>Ô>€BˆÐ>Ð>Ñ>Ø

€I€IIØ	€H€HHØ€K€KKØ

€I€IIØ€K€KKð €N€NNØ€O€OOØ€O€OOØÐÐÑØ€N€NNØÐÐÑØÐÐÑØ€O€OOØÐÐÑØ Ð Ð Ñ ØÐÐÑØÐÐÑØÐÐÑØÐÐÑàÐÐÑØ€K€KKØ˜%Ð0RÐ0RÐSÑSÔS€IˆxÐSÐSÑSÐSÐSr#   r   c                   óÎ   — e Zd ZU eed<   eed<   eed<   eed<   eed<   eed<   eed <   eed<   eed	<   eed
<   eed
<   eed<   eed
<   eed<   eed<   eed<   eed<   eed<   eed<   dS )ÚPatientAssessmentCreater(   r)   r*   r+   r,   r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   N)rA   rB   rC   r   rE   rF   r"   r#   r$   rH   rH   B   sØ   € € € € € € Ø

€I€IIØ	€H€HHØ€K€KKØ

€I€IIØ€K€KKà€N€NNØ€O€OOØ€O€OOØÐÐÑØ€N€NNØÐÐÑØÐÐÑØ€O€OOØÐÐÑØ Ð Ð Ñ ØÐÐÑØÐÐÑØÐÐÑØÐÐÑÐÐr#   rH   c                   ó$   — e Zd ZU eed<   eed<   dS )Ú
AdminLoginÚusernameÚpasswordN)rA   rB   rC   r   rE   r"   r#   r$   rJ   rJ   X   s"   € € € € € € Ø€M€MMØ€M€MM€M€Mr#   rJ   c                   ó$   — e Zd ZU eed<   eed<   dS )ÚAdminLoginResponseÚ successÚ messageN)rA   rB   rC   ÚboolrE   r   r"   r#   r$   rN   rN   \   s"   € € € € € € Ø
€M€MMØ
€L€LL€L€Lr#   rN   ÚdataÚreturnc                 ó  — | j         | j        z   | j        z   | j        z   | j        z   | j        z   | j        z   | j         z   | j        z   | j	        z   | j
        z   | j
        z   | j        z   | j
        z   }|dk    rd}n
|dk    rd}nd}||fS )Né+   z
Ama Presenté   zAma slightly presentzAma not present)r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   )rR   r;   r<   s      r$   Úcalculate_assessment_resultrW   a   sÕ   € àŒ˜œÑ(¨4¬?Ñ:ØÔñ	Ø!%¤ñ	0Ø26Ô2Eñ	FàÔñ	à#œñ	/à15Ô1Fñ	Gð 	
Ô$ñ 	%ð (,Ô'?ñ 	@ð 	
Ôñ		 ð #'Ô"4ñ		5ð 8<Ô7Oñ		Pð ð bÒ Ð ØˆˆØ	˜Ò	Ð	Ø'ˆˆà"ˆà
˜Ð
Ðr#   ú/c               ƒ   ó   K  — ddiS )NrP   zKamch Aam Parikshan APIr"   r"   r#   r$   ÚrootrZ   u   s   è è € àÐ0Ð
1Ð1r#   z
/assessment)Úresponse_modelÚinputc              ƒ   ó.  K  — t          | ¦  «        \  }}|                      ¦   «         }||d<   ||d<   t          di |¤Ž}|                     ¦   «         }|d                              ¦   «         |d<   t          j                             |¦  «        ƒ d {V —† |S )Nr;   r<   r@   r"   ) rW   Ú
model_dumpr   Ú	isoformatÚdbÚ
assessmentsÚ
insert_one)r\   r;   r<   Úassessment_dictÚassessment_objÚdocs         r$   Úsubmit_assessmentrf   y   s²   è è € õ 6°eÑ<Ô<Ñ€Kð ×&Ò&Ñ(Ô(€OØ%0€OMÑ"Ø &€OHÑÝ&Ð9Ð9¨Ð9Ð9€Nð 
×
#Ò
#Ñ
%Ô
%€CØ˜;Ô'×1Ò1Ñ3Ô3€Cˆ
Ñõ 

Œ.×
#Ò
# CÑ
(Ô
(Ð(Ð(Ð(Ð(Ð(Ð(Ð(à
Ðr#   z/admin/loginÚ
credentialsc              ƒ   óŠ   K  — | j         t          k    r!| j        t          k    rt	          dd¬¦  «        S t
          dd¬¦  «        ‚) NTzLogin successful)rO   rP   i‘  zInvalid credentials)Ú
status_codeÚdetail)rK   ÚADMIN_USERNAMErL   ÚADMIN_PASSWORDrN   r   )rg   s    r$   Ú
admin_loginrm      sI   è è € à Ô ~Ò -Ð -°+Ô2FÍ.Ò2XÐ2XÝ!¨$Ð8JÐKÑKÔKÐKå¨Ð4IÐJÑJÔJÐJr#   z/admin/assessmentsc               ƒ   ó*  K  — t           j                             i ddi¦  «                             d¦  «        ƒ d {V —†} | D ]:}t	          |d         t
          ¦  «        rt
          j         |d         ¦  «        |d<   Œ;|                      d„ d¬ ¦  «         | S )NÚ_idr   i'  r@   c                 ó   — | d         S )Nr@   r"   )Úxs    r$   r%   z%get_all_assessments.<locals>.<lambda>Ÿ   s
   €  1 [¤>€ r#   T)ÚkeyÚ reverse)	r`   ra   ÚfindÚ to_listÚ
isinstancer   r   Ú
fromisoformatÚsort)ra   Ú
assessments     r$   Úget_all_assessmentsrz   ”   s®   è è € õ œ×+Ò+¨B°¸°
Ñ;Ô;×CÒCÀEÑJÔJÐJÐJÐJÐJÐJÐJ€Kð "ð Vð Vˆ
Ý
j Ô-­sÑ
3Ô
3ð 	VÝ&.Ô&<¸ZÈ
Ô=TÑ&UÔ&UˆJ{Ñ#øð ×ÒÐ1Ð1¸4ÐÑ@Ô@Ð@à
Ðr#   TÚCORS_ORIGINSÚ*ú,)Úallow_credentialsÚ
allow_originsÚ
allow_methodsÚ
allow_headersz4%(asctime)s - %(name)s - %(levelname)s - %(message)s)ÚlevelÚformatÚshutdownc               ƒ   ó<   K  — t                                ¦   «          d S r   )ÚclientÚcloser"   r#   r$   Úshutdown_db_clientrˆ   µ   s   è è € å
‡L‚LN„N€N€N€Nr#   )AÚ fastapir   r   r   r   Úfastapi.securityr    r   Údotenvr	   Ústarlette.middleware.corsr
   Úmotor.motor_asyncior
   ÚosÚ loggingÚ pathlibr   Úpydanticr
   r   r   Útypingr   r   r    r   r   Ú secretsÚ__file__ÚparentÚROOT_DIRÚ environÚ	mongo_urlr†   r`   ÚappÚ
api_routerÚsecurityrk   rl   r   rH   rJ   rN   ÚtuplerF   r   rW   ÚgetrZ   Úpostrf   rm   rz   Úinclude_routerÚadd_middlewareÚsplitÚ
basicConfigÚINFOÚ	getLoggerrA   ÚloggerÚon_eventrˆ   r"   r#   r$   ú<module>r§      s  ðØ >Ð >Ð >Ð >Ð >Ð >Ð >Ð >Ð >Ð >Ð >Ð >Ø <Ð <Ð <Ð <Ð <Ð <Ð <Ð <Ø Ð Ð Ð Ð Ð Ø 4Ð 4Ð 4Ð 4Ð 4Ð 4Ø 2Ð 2Ð 2Ð 2Ð 2Ð 2Ø 	€	€	€	Ø €€€Ø Ð Ð Ð Ð Ð Ø 1Ð 1Ð 1Ð 1Ð 1Ð 1Ð 1Ð 1Ð 1Ð 1Ø !Ð !Ð !Ð !Ð !Ð !Ð !Ð !Ø 
€
€
€
Ø 'Ð 'Ð 'Ð 'Ð 'Ð 'Ð 'Ð 'Ø €€€à
ˆ4‰>Œ>Ô
 €Ø 
€
ˆHvÑÑ Ô Ð ð 
ŒJ{Ô#€	Ø	Ð	˜IÑ	&Ô	&€Ø
ˆBŒJyÔ!Ô"€ð  €gi„i€ð ˆY˜fÐ
%Ñ
%Ô
%€
ð ˆ9‰;Œ;€à€Ø €ðTð Tð Tð Tð T˜	ñ Tô Tð Tð<ð ð ð ð ˜iñ ô ð ð,ð ð ð ð ñ ô ð ðð ð ð ð ˜ñ ô ð ð
Ð&=ð À%ÈÈSÈÄ/ð ð ð ð ð( ‡‚ÑÔð2ð 2ñ Ôð2ð ‡‚Ð/@€ÑAÔAðÐ#:ð ð ð ñ BÔAðð& ‡‚Ð0B€ÑCÔCðK :ð Kð Kð Kñ DÔCðKð ‡‚Ð$°TÐ:KÔ5L€ÑMÔMðð ñ NÔMðð × Ò :Ñ Ô Ð à × Ò ØØØ”*—.’. °Ñ5Ô5×;Ò;¸CÑ@Ô@Ø%Ø%ð
 ñ ô ð ð € Ô Ø
Œ,Ø
Aðñ ô ð ð 
ˆÔ	˜8Ñ	$Ô	$€à‡‚ˆjÑÔðð ñ Ôðð ð r#   
