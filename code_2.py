import sqlite3
import os
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    username TEXT,
    password TEXT
)
""")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(user_id, username, password):
    if not isinstance(user_id, int) or not username or not password:
        raise ValueError("Invalid input data")

    query = "INSERT INTO users VALUES (?, ?, ?)"
    cursor.execute(query, (user_id, username, hash_password(password)))
    conn.commit()

def search_user(user_id):
    if not isinstance(user_id, int):
        raise ValueError("Invalid user ID")

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()

admin_user = os.getenv("ADMIN_USER")
admin_pass = os.getenv("ADMIN_PASS")

def login(username, password):
    if username == admin_user and hash_password(password) == admin_pass:
        return True
    return False