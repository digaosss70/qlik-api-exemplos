from dotenv import load_dotenv
import os
from qlik_sdk import AuthType, Config, Qlik

load_dotenv()

QLIK_HIOST = os.getenv("host")
QLIK_API_KEY = os.getenv("api_key")

auth = Qlik(Config(host=QLIK_HIOST, auth_type=AuthType.APIKey, api_key=QLIK_API_KEY))

items = auth.items.get_items(resourceType='app',limit=100)
item_names = []

for item in items.pagination:
    #item_names.append(item.name)
    print(item.name)

print(len(item_names))