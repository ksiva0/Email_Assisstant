import base64
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import config

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/userinfo.email'
]

def authenticate_gmail(user_email):
    creds = None
    token_file = f'token_{user_email}.pickle'

    # Load credentials if they exist
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials, initiate OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                config.GOOGLE_OAUTH_CONFIG, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except Exception as e:
        print(f"Error building Gmail service: {e}")
        return None

def fetch_emails(service, query=""):
    try:
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        emails = []

        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
            email_data = {
                'id': msg['id'],
                'sender': next(header['value'] for header in msg_data['payload']['headers'] if header['name'] == 'From'),
                'subject': next(header['value'] for header in msg_data['payload']['headers'] if header['name'] == 'Subject'),
                'timestamp': msg_data['internalDate'],
                'body': base64.urlsafe_b64decode(msg_data['payload']['parts'][0]['body']['data']).decode('utf-8', errors='ignore'),
                'thread_id': msg_data['threadId']
            }
            emails.append(email_data)
        return emails
    except HttpError as error:
        print(f'An error occurred while fetching emails: {error}')
