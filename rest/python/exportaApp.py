import requests
import json
from datetime import datetime, timedelta
import time
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

QLIK_HOST = os.getenv("host")
QLIK_API_KEY = os.getenv("api_key")

qHeader = headers={"Authorization": f"Bearer {QLIK_API_KEY}", "Content-Type": "application/json"}
qHeader2 = headers={"Authorization": f"Bearer {QLIK_API_KEY}"}


def exportaApp(appId):
    url = f"{QLIK_HOST}/api/v1/apps/{appId}/export"
    response = requests.post(url, headers=qHeader2, timeout=240)
    print(response.status_code)
    print(response.text)



exportaApp('ae088002-6066-45e6-95e9-f2dd1f97f023')