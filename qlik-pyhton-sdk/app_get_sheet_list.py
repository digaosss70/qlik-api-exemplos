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

# app is fetched from the REST /v1/apps/{app_id}
app = auth.get(QLIK_APP_ID)

sheetListProps = {
  "qInfo": {
    "qType": "SheetList",
    "qId": ""
  },
  "qAppObjectListDef": {
    "qData": {
      "title": "/qMetaDef/title",
      "labelExpression": "/labelExpression",
      "showCondition": "/showCondition",
      "description": "/qMetaDef/description",
      "descriptionExpression": "/qMetaDef/descriptionExpression",
      "thumbnail": "/qMetaDef/thumbnail",
      "cells": "/cells",
      "rank": "/rank",
      "columns": "/columns",
      "rows": "/rows",
      "ownerId": "/qMetaDef/ownerId"
    },
    "qType": "sheet"
  }
}

with app.open():
  
    session_obj = app.create_session_object(json.loads(json.dumps(sheetListProps)))
    sheet_list_layout = session_obj.get_layout()

    print(sheet_list_layout)

    #for s in sheet_list_layout.qAppObjectList.qItems:
        #print(f" id {s.qInfo.qId} title {s.qData.title} up {s.qData.ownerId}")
