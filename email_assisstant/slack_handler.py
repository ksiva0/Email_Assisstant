import requests  
from config import SLACK_BOT_TOKEN  

def send_slack_message(channel, message):  
    headers = {  
        'Authorization': f'Bearer {SLACK_BOT_TOKEN}',  
        'Content-Type': 'application/json'  
    }  
    data = {  
        'channel': channel,  
        'text': message  
    }  
    response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, json=data)  
    return response.json()  
