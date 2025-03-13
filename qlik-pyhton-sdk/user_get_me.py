from dotenv import load_dotenv
import os
from qlik_sdk import Auth, AuthType, Config, Apps

# Carrega as variáveis de ambiente
load_dotenv()

QLIK_HIOST = os.getenv("host")
QLIK_CLIENT_ID = os.getenv("client_id")
QLIK_CLIENT_SECRET = os.getenv("client_secret")


# define the OAuth2 client configuration
# host in the format like https://screenshot.us.qlikcloud.com
client = Auth(
    config=Config(
        auth_type=AuthType.OAuth2,
        host=QLIK_HIOST,
        client_id=QLIK_CLIENT_ID,
        client_secret=QLIK_CLIENT_SECRET,
    )
)

# authorize the client configuration with your Qlik Cloud tenant
client.authorize()

# call the /users/me rest endpoint with the client configuration
response = client.rest(path="/users/me")
print(response.json())
