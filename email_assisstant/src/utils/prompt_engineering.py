import openai
import streamlit as st

openai.api_key = st.secrets["openai"]["api_key"]

def understand_email(email):
    prompt = f"Analyze the following email and determine the sender's intent:\n\n{email['body']}\n\nRespond with JSON: {{'action': '...', 'details': {{...}}}}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        return eval(response.choices[0].message.content)
    except Exception:
        return {"action": "notify"}
