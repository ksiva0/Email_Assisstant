import os  
import base64  
import google_auth_oauthlib.flow  
import googleapiclient.discovery  
from googleapiclient.errors import HttpError  
from config import GOOGLE_API_CREDENTIALS  

def authenticate_gmail():  
    try:  
        print(f"Using credentials file: {GOOGLE_API_CREDENTIALS}")  # Debug statement  
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(  
            GOOGLE_API_CREDENTIALS,  
            scopes=['https://www.googleapis.com/auth/gmail.readonly'])  
        credentials = flow.run_local_server(port=0)  
        return googleapiclient.discovery.build('gmail', 'v1', credentials=credentials)  
    except Exception as e:  
        print(f"Error during authentication: {e}")  # Print any authentication errors  
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
                'sender': msg_data['payload']['headers'][0]['value'],  
                'subject': msg_data['payload']['headers'][1]['value'],  
                'timestamp': msg_data['internalDate'],  
                'body': base64.urlsafe_b64decode(msg_data['payload']['parts'][0]['body']['data'].encode('UTF-8')),  
                'thread_id': msg_data['threadId']  
            }  
            emails.append(email_data)  
        return emails  
    except HttpError as error:  
        print(f'An error occurred: {error}')  
        return []  
