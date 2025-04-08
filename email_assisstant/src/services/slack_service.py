from slack_sdk import WebClient
import streamlit as st

client = WebClient(token=st.secrets["slack"]["bot_token"])

def notify_slack(message):
    client.chat_postMessage(channel=st.secrets["slack"]["channel_id"], text=str(message))
