import streamlit as st  
from email_handler import authenticate_gmail, fetch_emails  
from database import init_db, insert_email  
from llm_handler import generate_reply  
from slack_handler import send_slack_message  
from calendar_handler import create_event  

def main():  
    st.title('AI-Powered Personal Email Assistant')  
    
    # Authenticate to Gmail  
    service = authenticate_gmail()  
    if service:  
        st.success("Successfully authenticated with Gmail.")  
        emails = fetch_emails(service)  
        for email in emails:  
            insert_email(email)  # Store email in DB  
            st.write(f"From: {email['sender']}, Subject: {email['subject']}")  

            # Generate a reply for the email  
            if st.button(f"Generate Reply for {email['subject']}"):  
                reply = generate_reply(email['body'])  
                st.text_area("Generated Reply:", reply)  

                # Optional: send reply to Slack or create calendar event  
                # send_slack_message(channel='your_channel_id', message=reply)  
                # create_event(event_data) - Define event_data as per your needs  

    else:  
        st.error("Failed to authenticate with Gmail.")  

if __name__ == "__main__":  
    init_db()  
    main()  
