import openai  
from config import OPENAI_API_KEY  

openai.api_key = OPENAI_API_KEY  

def generate_reply(email_body):  
    response = openai.ChatCompletion.create(  
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": f"Draft a response for the following email: {email_body}"}]  
    )  
    return response['choices'][0]['message']['content']  
