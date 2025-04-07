import sqlite3  
from config import DATABASE_URI  

def init_db():  
    conn = sqlite3.connect(DATABASE_URI)  
    cursor = conn.cursor()  
    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS emails (  
            id INTEGER PRIMARY KEY,  
            sender TEXT,  
            recipient TEXT,  
            subject TEXT,  
            timestamp DATETIME,  
            body TEXT,  
            thread_id TEXT  
        )  
    ''')  
    conn.commit()  
    conn.close()  

def insert_email(email_data):  
    conn = sqlite3.connect(DATABASE_URI)  
    cursor = conn.cursor()  
    cursor.execute('''  
        INSERT INTO emails (sender, recipient, subject, timestamp, body, thread_id)  
        VALUES (?, ?, ?, ?, ?, ?)''',   
        (email_data['sender'], email_data['recipient'], email_data['subject'],  
         email_data['timestamp'], email_data['body'], email_data['thread_id']))  
    conn.commit()  
    conn.close()  
