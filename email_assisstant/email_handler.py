import base64  
import google.auth  
import googleapiclient.discovery  
from googleapiclient.errors import HttpError  
import config  

def authenticate_gmail():  
    # Create credentials from the service account info in config  
    try:  
        credentials = google.oauth2.service_account.Credentials.from_service_account_info(config.GOOGLE_CREDENTIALS)  

        # Build the Gmail service  
        service = googleapiclient.discovery.build('gmail', 'v1', credentials=credentials)  
        return service  
    except Exception as e:  
        print(f"Error during authentication: {e}")  # Print any authentication errors  
        return None  

def fetch_emails(service, query=""):  
    try:  
        # List user messages  
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
                'body': base64.urlsafe_b64decode(msg_data['payload']['parts'][0]['body']['data'].encode('UTF-8')).decode('utf-8', errors='ignore'),  
                'thread_id': msg_data['threadId']  
            }  
            emails.append(email_data)  
        return emails  
    except HttpError as error:  
        print(f'An error occurred: {error}')  
        return []  
    except Exception as e:  
        print(f"An error occurred while fetching emails: {e}")  
        return []  
