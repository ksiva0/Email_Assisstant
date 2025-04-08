import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_email(content: str):
    prompt = f"Summarize this email thread: {content}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
