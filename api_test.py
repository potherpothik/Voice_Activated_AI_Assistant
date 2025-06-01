import requests
from config import DEEPGRAM_API_KEY

api_key = DEEPGRAM_API_KEY
headers = {"Authorization": f"Token {api_key}"}
response = requests.get("https://api.deepgram.com/v1/projects", headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
