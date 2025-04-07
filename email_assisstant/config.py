import os
import streamlit as st

# Accessing Streamlit secrets for sensitive data  
GOOGLE_CLIENT_ID = st.secrets["google"]["client_id"]  
GOOGLE_CLIENT_SECRET = st.secrets["google"]["client_secret"]
GOOGLE_CREDENTIALS = st.secrets["credentials"]

# Initialize the database name and path  
DB_NAME = 'email_assistant.db'  
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the current directory  
DATABASE_URI = os.path.join(BASE_DIR, DB_NAME)  # Create the absolute path to the database  

# OpenAI API key  
OPENAI_API_KEY = st.secrets["openai"]["OPENAI_API_KEY"]  

# Slack credentials  
SLACK_BOT_TOKEN = st.secrets["slack"]["SLACK_BOT_TOKEN"]
