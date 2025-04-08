import requests  
import config  

def send_slack_message(channel, message):  
    url = 'https://slack.com/api/chat.postMessage'  
    headers = {  
        'Authorization': f'Bearer {config.SLACK_BOT_TOKEN}',  
        'Content-Type': 'application/json'  
    }  
    data = {  
        'channel': channel,  
        'text': message  
    }  
    
    response = requests.post(url, headers=headers, json=data)  
    
    if not response.json().get('ok'):  
        print(f"Error sending message to Slack: {response.json()}")  
