import sqlite3  
from sqlite3 import Error  

def create_connection(db_file):  
    """ Create a database connection to the SQLite database specified by db_file """  
    conn = None  
    try:  
        conn = sqlite3.connect(db_file)  
        return conn  
    except Error as e:  
        print(e)  
    return conn  

def create_table(conn):  
    """ Create a table in the database """  
    create_emails_table = """  
    CREATE TABLE IF NOT EXISTS emails (  
        id TEXT PRIMARY KEY,  
        sender TEXT NOT NULL,  
        recipient TEXT NOT NULL,  
        subject TEXT NOT NULL,  
        timestamp INTEGER,  
        body TEXT  
    );"""  
    try:  
        c = conn.cursor()  
        c.execute(create_emails_table)  
    except Error as e:  
        print(e)  

def store_email(conn, email):  
    """ Store an email in the database """  
    sql = '''INSERT OR REPLACE INTO emails(id, sender, recipient, subject, timestamp, body)  
              VALUES(?, ?, ?, ?, ?, ?)'''  
    cur = conn.cursor()  
    cur.execute(sql, email)  
    conn.commit()  
