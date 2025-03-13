from dotenv import load_dotenv
import os
from qlik_sdk import Apps, AuthType, Config, Qlik
import json

# Carrega as variáveis de ambiente
load_dotenv()

QLIK_HIOST = os.getenv("host")
QLIK_API_KEY = os.getenv("api_key")
QLIK_APP_ID = os.getenv("app_id")

auth = Apps(Config(host=QLIK_HIOST, auth_type=AuthType.APIKey, api_key=QLIK_API_KEY))


app = auth.get(QLIK_APP_ID)

#publicar
#app.publish({"spaceId": "<SPACE_ID>"})

#republicar
app.set_publish({
    "targetId": "<APP_TARGE_ID>",
    "checkOriginAppId":False,
    "data":"target" #source
    })

