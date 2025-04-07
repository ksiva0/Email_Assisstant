from googleapiclient.discovery import build  
from config import GOOGLE_API_CREDENTIALS  

def create_event(event):  
    service = build('calendar', 'v3', credentials=authenticate_gmail())  # You might want to refactor this  
    event_result = service.events().insert(calendarId='primary', body=event).execute()  
    return event_result  
