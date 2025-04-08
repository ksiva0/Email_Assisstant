import sqlite3

def save_email_to_db(email):
    conn = sqlite3.connect("emails.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emails (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 sender TEXT,
                 subject TEXT,
                 timestamp TEXT,
                 body TEXT)''')
    c.execute("INSERT INTO emails (sender, subject, timestamp, body) VALUES (?, ?, ?, ?)",
              (email['sender'], email['subject'], email['timestamp'], email['body']))
    conn.commit()
    conn.close()
