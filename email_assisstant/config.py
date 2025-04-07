import os  

# Define the database name and path  
DB_NAME = 'email_assistant.db'  
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the current directory  
DATABASE_URI = os.path.join(BASE_DIR, DB_NAME)  # Create the absolute path to the database  

# Google API credentials  
GOOGLE_API_CREDENTIALS = 'path/to/credentials.json'  

# OpenAI API key  
OPENAI_API_KEY = 'your_openai_api_key'  

# Slack credentials  
SLACK_BOT_TOKEN = 'your_slack_bot_token'  

# Database connection  
DATABASE_URI = 'sqlite:///email_assistant.db'  # Or PostgreSQL connection string  
