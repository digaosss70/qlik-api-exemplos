from dotenv import load_dotenv
import os
from qlik_sdk import Apps, AuthType, Config, Qlik
import json

# Carrega as variáveis de ambiente
load_dotenv()

QLIK_HIOST = os.getenv("host")
QLIK_API_KEY = os.getenv("api_key")
QLIK_APP_ID = os.getenv("app_id")

auth = Qlik(Config(host=QLIK_HIOST, auth_type=AuthType.APIKey, api_key=QLIK_API_KEY))

lista_de_apps = auth.items.get_items(resourceType='app', limit=1,name=f)