from sqlalchemy import Column, Integer, String, DateTime
from database.db import Base

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    recipient = Column(String)
    subject = Column(String)
    body = Column(String)
    timestamp = Column(DateTime)
