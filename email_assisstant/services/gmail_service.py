from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def get_gmail_service():
    creds = Credentials(
        token=os.getenv("ACCESS_TOKEN"),
        refresh_token=os.getenv("REFRESH_TOKEN"),
        token_uri=os.getenv("token_uri"),
        client_id=os.getenv("client_id"),
        client_secret=os.getenv("client_secret")
    )
    return build("gmail", "v1", credentials=creds)

def fetch_emails():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])
    return messages
