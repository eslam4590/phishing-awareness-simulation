import requests
import json

API_KEY = "YOUR_GOPHISH_API_KEY"
GOPHISH_URL = "http://localhost:3333/api"

# Replace with actual IDs from your GoPhish setup
campaign_data = {
    "name": "Awareness Campaign - April",
    "template": {"name": "Password Reset Alert"},
    "url": "http://fake-login.acmecorp.com",
    "launch_date": "",
    "smtp": {"name": "Internal Mailer"},
    "groups": [{"name": "Test Employees"}]
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def create_campaign():
    response = requests.post(
        f"{GOPHISH_URL}/campaigns/?api_key={API_KEY}",
        headers=headers,
        data=json.dumps(campaign_data)
    )
    if response.status_code == 201:
        print("Campaign successfully created and launched.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

create_campaign()
