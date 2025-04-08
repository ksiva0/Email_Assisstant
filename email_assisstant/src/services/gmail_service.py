import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import streamlit as st

def fetch_emails():
    creds = Credentials(
        token=None,
        refresh_token=st.secrets["gmail"]["refresh_token"],
        token_uri='https://oauth2.googleapis.com/token',
        client_id=st.secrets["gmail"]["client_id"],
        client_secret=st.secrets["gmail"]["client_secret"]
    )
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_detail['payload']
        headers = {h['name']: h['value'] for h in payload['headers']}
        body = base64.urlsafe_b64decode(payload['body'].get('data', '')).decode('utf-8', errors='ignore')
        emails.append({
            "sender": headers.get("From"),
            "subject": headers.get("Subject"),
            "timestamp": headers.get("Date"),
            "body": body
        })
    return emails
