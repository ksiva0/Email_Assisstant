from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

def create_event(summary, start_time, end_time):
    credentials = service_account.Credentials.from_service_account_file("calendar-credentials.json")
    service = build("calendar", "v3", credentials=credentials)

    event = {
        "summary": summary,
        "start": {"dateTime": start_time, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end_time, "timeZone": "Asia/Kolkata"},
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get("htmlLink")
