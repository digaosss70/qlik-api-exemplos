#!python3 -m pip install qlik-sdk
#!python3 -m pip install boto

from qlik_sdk import Apps, AuthType, Config, Qlik
import shutil
import boto3
import re

QLIK_HOST = 'https://<QLIK_HOST >.us.qlikcloud.com'
QLIK_API_KEY = '<QLIK_API_KEY>'
QLIK_APP_ID='<QLIK_APP_ID>'

AWS_ACCESS_KEY_ID = "<AWS_ACCESS_KEY_ID >"
AWS_SECRET_ACCESS_KEY = "<AWS_SECRET_ACCESS_KEY>"
AWS_REGION = "<AWS_REGION>"
BUCKET_NAME = "<BUCKET_NAME>"

# mkdir /tmp/qlik

config = Config(host=QLIK_HOST, auth_type=AuthType.APIKey, api_key=QLIK_API_KEY)

apps = Apps(config=config)
qlik = Qlik(config=config)

app = apps.get(QLIK_APP_ID)
app_nome_limpo = re.sub(r'[^a-zA-Z0-9]', '', app.attributes.name)

file_path = "/tmp/qlik/"
file_name = f"{QLIK_APP_ID}_{app.attributes.name}.qvf"
file_name_limpo = f"{QLIK_APP_ID}_{app_nome_limpo}.qvf"

temp_contents_url = app.export(True)
local_filename = f"{file_path}{file_name_limpo}"
with qlik.rest(path=temp_contents_url, method="get", stream=True) as r:
    with open(local_filename, "wb") as f:
        shutil.copyfileobj(r.raw, f)
print(f"Exported: {QLIK_APP_ID}_{app.attributes.name} to: {local_filename}")


s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

try:
    s3_client.upload_file(
        local_filename,
        BUCKET_NAME,
        f"qlik/{file_name}"
    )
    print(f"File '{local_filename}' successfully uploaded to S3 bucket '{BUCKET_NAME}' as '{file_name}'.")
except Exception as e:
    print(f"Error uploading file '{local_filename}' to S3: {e}")            
