import googleapiclient.discovery  
import google.oauth2.service_account  
import config  

def authenticate_calendar():  
    try:  
        # Create credentials from service account info in config  
        credentials = google.oauth2.service_account.Credentials.from_service_account_info(config.CALENDAR_CREDENTIALS)  

        # Specify the Calendar scope  
        scopes = ['https://www.googleapis.com/auth/calendar']  

        # Add the required scopes  
        scoped_credentials = credentials.with_scopes(scopes)  

        # Build the Google Calendar service  
        service = googleapiclient.discovery.build('calendar', 'v3', credentials=scoped_credentials)  
        return service  
    except Exception as e:  
        print(f"Error during calendar authentication: {e}")  
        return None  

def create_event(service, event_details):  
    try:  
        event = service.events().insert(calendarId='primary', body=event_details).execute()  
        return event  
    except Exception as e:  
        print(f"An error occurred while creating the event: {e}")  
        return None  
