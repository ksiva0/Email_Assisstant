import streamlit as st  
from email_handler import authenticate_gmail, fetch_emails  
from database import init_db, insert_email  
from llm_handler import generate_reply  
from slack_handler import send_slack_message   
from calendar_handler import authenticate_calendar, create_event  

def main():  
    st.title("AI-Powered Personal Email Assistant")  

    # Authenticate Gmail  
    gmail_service = authenticate_gmail()  
    if gmail_service:  
        st.success("Successfully authenticated with Gmail.")  
        emails = fetch_emails(gmail_service)  
        st.write("Emails fetched successfully:", emails)  

    else:  
        st.error("Failed to authenticate with Gmail.")  

    # Authenticate Google Calendar  
    calendar_service = authenticate_calendar()  
    if calendar_service:  
        st.success("Successfully authenticated with Google Calendar.")  
        
        # You can call create_event function here when you have event details  
        # Example to create an event (replace event_details with actual data)  
        event_details = {  
            'summary': 'Test Event',  
            'start': {  
                'dateTime': '2023-10-01T09:00:00-07:00',  # Update with actual event start time  
                'timeZone': 'America/Los_Angeles',  
            },  
            'end': {  
                'dateTime': '2023-10-01T10:00:00-07:00',  # Update with actual event end time  
                'timeZone': 'America/Los_Angeles',  
            },  
        }  
        event = create_event(calendar_service, event_details)  
        if event:  
            st.write("Event created successfully:", event)  

    else:  
        st.error("Failed to authenticate with Google Calendar.")  

if __name__ == "__main__":  
    main()  
