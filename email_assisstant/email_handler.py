import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import config

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/userinfo.email'
]

def authenticate_gmail(user_email):
    try:
        # Load credentials from service account config
        credentials = service_account.Credentials.from_service_account_info(
            config.GOOGLE_CREDENTIALS,  # this should be your dict from secrets
            scopes=SCOPES
        )

        # Impersonate the user
        delegated_credentials = credentials.with_subject(user_email)

        # Build Gmail service
        service = build('gmail', 'v1', credentials=delegated_credentials)
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
        return []
