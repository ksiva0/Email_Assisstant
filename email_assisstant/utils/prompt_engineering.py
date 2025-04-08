def create_summary_prompt(email_body: str) -> str:
    return f"Summarize this email:
\n{email_body}\n\nSummary:"
