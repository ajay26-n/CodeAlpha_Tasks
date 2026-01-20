import sqlite3
import hashlib


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")


password = "admin123"
hashed_password = hashlib.sha256(password.encode()).hexdigest()

cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("admin", hashed_password)
)

conn.commit()
conn.close()

print("Database created successfully with sample user.")