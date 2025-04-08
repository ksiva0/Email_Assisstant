from fastapi import APIRouter
from controllers import email_controller

router = APIRouter()

@router.get("/process")
def trigger_processing():
    email_controller.process_emails()
    return {"status": "Emails processed"}
