import requests
import json
from datetime import datetime, timedelta
import time
import os
from pathlib import Path
from dotenv import load_dotenv
import pytz

load_dotenv()

QLIK_HOST = os.getenv("HOST")
QLIK_API_KEY = os.getenv("API_KEY")

qHeader = headers={"Authorization": f"Bearer {QLIK_API_KEY}", "Content-Type": "application/json"}
qHeader2 = headers={"Authorization": f"Bearer {QLIK_API_KEY}"}

def getSpaceIdByName(spaceName):
    response = requests.request("GET", f"{QLIK_HOST}:443/api/v1/spaces?filter=NAME eq \"{spaceName}\"", headers=qHeader)
    jsonResponse = json.loads(response.text)['data']

    if jsonResponse:
        return jsonResponse[0]['id']
    else: 
        return None

def getconnectionIdBySpaceId(spaceId):
    response = requests.request("GET", f"{QLIK_HOST}:443/api/v1/data-files/connections?spaceId={spaceId}", headers=qHeader)
    jsonResponse = json.loads(response.text)['data']

    if jsonResponse:
        return jsonResponse[0]['id']
    else: 
        return None
    
def getItem(fileName,spaceId):
    response = requests.request("GET", f"{QLIK_HOST}:443/api/v1/items?&query={fileName}&spaceId={spaceId}", headers=qHeader)
    jsonResponse = json.loads(response.text)['data']

    if jsonResponse:
        dateInfo = datetime.strptime(jsonResponse[0]['updatedAt'], "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=3)

        itemResponse = {
            'itemId' : jsonResponse[0]['resourceAttributes']['sourceSystemId'][7:],
            'updateDate': datetime.fromisoformat(str(dateInfo)[0:19])
        }
        #return jsonResponse[0]['resourceAttributes']['sourceSystemId'][7:]
        return itemResponse
    else:
        return None    

def createItem(itemName,folder,connectionId):
    filePath = os.path.join(folder, itemName)
    url = f"{QLIK_HOST}/api/v1/data-files"
 
    files = {
    		'File': (f"{itemName}", open(filePath, 'rb')),
    		'Json': (None, f'{{"name":"{itemName}","connectionId":"{connectionId}"}}', 'application/json')
	}

    response = requests.post(url, headers=qHeader2, files=files)
    return response.status_code

def updateItem(itemId,itemName,folder,connectionId):
    filePath = os.path.join(folder, itemName)
    url = f"{QLIK_HOST}/api/v1/data-files/{itemId}"
 
    files = {
    		'File': (f"{itemName}", open(filePath, 'rb')),
    		'Json': (None, f'{{"name":"{itemName}","connectionId":"{connectionId}"}}', 'application/json')
	}

    response = requests.put(url, headers=qHeader2, files=files)
    return response.status_code

def deleteItem(itemId):
    url = f"{QLIK_HOST}/api/v1/data-files/{itemId}"

    response = requests.delete(url, headers=qHeader2)
    return response.status_code   
