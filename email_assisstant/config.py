import os
import streamlit as st

# Accessing Streamlit secrets for sensitive data  
GOOGLE_CLIENT_ID = st.secrets["google"]["client_id"]  
GOOGLE_CLIENT_SECRET = st.secrets["google"]["client_secret"]
GOOGLE_CREDENTIALS = st.secrets["credentials"]
CALENDAR_CREDENTIALS = st.secrets["calendar"]
WEB_SEARCH_API_KEY = st.secrets["google"]["GOOGLE_API_KEY"]


GOOGLE_OAUTH_CONFIG = {
    "installed": {
        "client_id":GOOGLE_CLIENT_ID,
      "project_id":"able-math-455408-b1",
      "auth_uri":"https://accounts.google.com/o/oauth2/auth",
      "token_uri":"https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
      "client_secret":GOOGLE_CLIENT_SECRET,
      "redirect_uris":["https://api.slack.com/apps/A08L8C9RZPU/oauth?"]
    }
}


# Initialize the database name and path  
DB_NAME = 'email_assistant.db'  
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the current directory  
DATABASE_URI = os.path.join(BASE_DIR, DB_NAME)  # Create the absolute path to the database  

# OpenAI API key  
OPENAI_API_KEY = st.secrets["openai"]["OPENAI_API_KEY"]  

# Slack credentials  
SLACK_BOT_TOKEN = st.secrets["slack"]["SLACK_BOT_TOKEN"]
