import sqlite3  
from config import DATABASE_URI  

def init_db():  
    try:  
        # Connecting to the SQLite database  
        conn = sqlite3.connect(DATABASE_URI)  
        cursor = conn.cursor()  

        # Create table if it doesn't exist  
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
            conn.close()  # Ensure the connection is closed after the operation  
