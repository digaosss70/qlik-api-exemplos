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

with app.open():
    app_info = app.get_app_layout()
    print(app_info)
    print(app_info.qTitle)

