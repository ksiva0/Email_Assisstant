import sqlite3  
from config import DATABASE_URI  

def init_db():  
    """Initialize the database and create email table if it doesn't exist."""  
    conn = None  # Initialize conn to None to ensure it is defined  
    try:  
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
        conn.commit()  # Commit the changes  
    except sqlite3.Error as e:  
        print(f"An error occurred: {e}")  # Print the error if one occurs  
    finally:  
        if conn:  
            conn.close()  # Ensure the connection is closed if it was created  

# The insert_email function remains unchanged  
def insert_email(email_data):  
    """Insert an email into the database."""  
    conn = sqlite3.connect(DATABASE_URI)  
    cursor = conn.cursor()  
    cursor.execute('''  
        INSERT INTO emails (sender, recipient, subject, timestamp, body, thread_id)  
        VALUES (?, ?, ?, ?, ?, ?)''',  
        (email_data['sender'], email_data['recipient'],  
         email_data['subject'], email_data['timestamp'],  
         email_data['body'], email_data['thread_id']))  
    conn.commit()  
    conn.close()  
