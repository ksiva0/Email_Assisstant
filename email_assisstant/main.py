import streamlit as st  
from email_handler import authenticate_gmail, fetch_emails  

def main():  
    st.title("Gmail API Tester")  

    user_email = 'mastersiva530@gmail.com'  

    # Authenticate Gmail  
    gmail_service = authenticate_gmail(user_email)  
    if gmail_service:  
        st.success("Successfully authenticated with Gmail.")  

        # Fetch emails and display them  
        emails = fetch_emails(gmail_service)  
        st.write("Fetched Emails:", emails)  
    else:  
        st.error("Failed to authenticate with Gmail.")  

if __name__ == "__main__":  
    main()  
