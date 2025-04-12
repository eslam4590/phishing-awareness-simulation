import requests
import pandas as pd

API_KEY = "YOUR_GOPHISH_API_KEY"
GOPHISH_URL = "http://localhost:3333/api"

def get_campaigns():
    response = requests.get(f"{GOPHISH_URL}/campaigns/?api_key={API_KEY}")
    return response.json()

def summarize_campaign(campaign_id):
    response = requests.get(f"{GOPHISH_URL}/campaigns/{campaign_id}?api_key={API_KEY}")
    data = response.json()

    events = data.get("timeline", [])
    df = pd.DataFrame(events)

    if not df.empty:
        print("Summary of Events:")
        print(df['message'].value_counts())
    else:
        print("No data found for this campaign.")

# Example usage
campaigns = get_campaigns()
if campaigns:
    summarize_campaign(campaigns[0]["id"])
else:
    print("No campaigns found.")
