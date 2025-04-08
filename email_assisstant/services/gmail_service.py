from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def get_gmail_service():
    creds = Credentials(
        token=os.getenv("GMAIL_ACCESS_TOKEN"),
        refresh_token=os.getenv("GMAIL_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("GMAIL_CLIENT_ID"),
        client_secret=os.getenv("GMAIL_CLIENT_SECRET"),
    )
    return build("gmail", "v1", credentials=creds)

def fetch_emails():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])
    return messages
