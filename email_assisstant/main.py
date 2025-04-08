import streamlit as st  
from email_handler import authenticate_gmail, fetch_emails  
from database_handler import create_connection, create_table, store_email  
from llm_handler import analyze_email_content  
from web_search import perform_web_search  
from slack_integration import send_slack_message  
from calendar_integration import create_calendar_event  

def main():  
    st.title("AI Personal Email Assistant")  

    user_email = st.text_input("Enter the email address you want to access:")  
    if st.button("Authenticate"):  
        gmail_service = authenticate_gmail(user_email)  
        if gmail_service:  
            st.success("Successfully authenticated with Gmail.")  
            emails = fetch_emails(gmail_service)  
            st.write("Emails fetched:", emails)  

            # Connect to database and create table  
            conn = create_connection("emails.db")  
            create_table(conn)  

            # Store emails in the database  
            for email in emails:  
                store_email(conn, (email['id'], email['sender'], user_email, email['subject'], email['timestamp'], email['body']))  

            # Analyze latest email content  
            if emails:  
                response = analyze_email_content(emails[0]['body'])  
                st.write("LLM Analysis:", response)  

            # Web Search Example  
            search_query = st.text_input("Search the web for:")  
            if st.button("Search"):  
                results = perform_web_search(search_query)  
                st.write("Search Results:", results)  

            # Slack Integration Example  
            slack_channel = st.text_input("Enter Slack channel to notify:")  
            if st.button("Notify Slack"):  
                send_slack_message(slack_channel, "Important email received!")  
                st.success("Message sent to Slack.")  

            # Calendar Event Scheduling Example  
            if st.button("Schedule Event"):  
                create_calendar_event("Meeting", "Description", "Location", "2023-10-15T10:00:00Z")  
                st.success("Event scheduled on Google Calendar.")  
        else:  
            st.error("Failed to authenticate with Gmail.")  

if __name__ == "__main__":  
    main()  
