import googleapiclient.discovery  
import google.oauth2.service_account  
import config  

def create_calendar_event(summary, description, location, start_time):  
    credentials = google.oauth2.service_account.Credentials.from_service_account_info(  
        config.CALENDAR_CREDENTIALS,  
        scopes=['https://www.googleapis.com/auth/calendar']  
    )  

    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)  

    event = {  
        'summary': summary,  
        'location': location,  
        'description': description,  
        'start': {  
            'dateTime': start_time,  
            'timeZone': 'America/Los_Angeles',  # Change to your timezone  
        },  
        'end': {  
            'dateTime': start_time,  # Adjust end time as needed  
            'timeZone': 'America/Los_Angeles',  
        },  
    }  

    event = service.events().insert(calendarId='primary', body=event).execute()  
    print('Event created: %s' % (event.get('htmlLink')))  
