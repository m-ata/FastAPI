import sqlite3

async def init_db():
    
    conn = sqlite3.connect("desktop_app.db")
    
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            fullname TEXT NOT NULL,
            hashpassword TEXT NOT NULL
        )"""
    )
    conn.commit()
    conn.close()
