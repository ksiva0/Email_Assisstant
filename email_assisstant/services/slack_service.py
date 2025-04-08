import requests
import os

def send_slack_notification(message: str):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    response = requests.post(webhook_url, json={"text": message})
    return response.status_code == 200
