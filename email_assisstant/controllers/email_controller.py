from services import gmail_service, llm_service, slack_service

def process_emails():
    emails = gmail_service.fetch_emails()
    for msg in emails:
        summary = llm_service.summarize_email("...email body here...")
        slack_service.send_slack_notification(summary)
