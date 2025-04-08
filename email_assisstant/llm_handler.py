import openai  
import config  

def analyze_email_content(email_content):  
    prompt = f"Analyze this email: {email_content}. What is the intent and how should I respond?"  
  
    response = openai.ChatCompletion.create(  
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": prompt}]  
    )  
    
    return response.choices[0].message['content']  
