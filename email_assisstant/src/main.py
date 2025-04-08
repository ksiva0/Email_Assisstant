import streamlit as st
from controllers.email_controller import process_emails

st.set_page_config(page_title="AI Email Assistant", layout="wide")
st.title("📬 AI Personal Email Assistant")

if st.button("Fetch & Process Emails"):
    process_emails()
    st.success("Emails fetched, processed, and actions triggered.")
