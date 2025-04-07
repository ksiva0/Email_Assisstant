import googleapiclient.discovery  
import config  

def create_event(service, event_details):  
    try:  
        event = service.events().insert(calendarId='primary', body=event_details).execute()  
        return event  
    except Exception as e:  
        print(f"An error occurred while creating the event: {e}")  
        return None  

def authenticate_calendar():  
    try:  
        # Create credentials from the service account info in config  
        credentials = google.oauth2.service_account.Credentials.from_service_account_info(config.GOOGLE_CREDENTIALS)  
        
        # Build the Google Calendar service  
        service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)  
        return service  
    except Exception as e:  
        print(f"Error during calendar authentication: {e}")  
        return None  
