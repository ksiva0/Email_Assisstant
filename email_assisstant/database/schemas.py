from pydantic import BaseModel
from datetime import datetime

class EmailSchema(BaseModel):
    sender: str
    recipient: str
    subject: str
    body: str
    timestamp: datetime

    class Config:
        orm_mode = True
