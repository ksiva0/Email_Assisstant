from services.gmail_service import fetch_emails
from utils.db import save_email_to_db
from utils.prompt_engineering import understand_email
from services.slack_service import notify_slack
from services.calendar_service import schedule_event
from services.web_search_service import maybe_search_web

def process_emails():
    emails = fetch_emails()
    for email in emails:
        save_email_to_db(email)
        context = understand_email(email)

        if context.get("action") == "schedule_meeting":
            schedule_event(context)
        elif context.get("action") == "web_search":
            result = maybe_search_web(context)
            notify_slack(result)
        elif context.get("action") == "notify":
            notify_slack(email)
