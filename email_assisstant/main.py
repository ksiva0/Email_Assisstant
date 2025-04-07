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
        # You can now call fetch_emails function or other functionality here  
        emails = fetch_emails(service)  
        st.write("Emails fetched successfully.", emails)  # Replace this with your actual function.  

    else:  
        st.error("Failed to authenticate with Gmail.")   

if __name__ == "__main__":  
    init_db()  
    main()  
