import sqlite3
import os

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    username TEXT,
    password TEXT
)
""")

def add_user(user_id, username, password):
    query = f"INSERT INTO users VALUES ({user_id}, '{username}', '{password}')"
    cursor.execute(query)
    conn.commit()

def search_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchall()

def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False

def backup_database(filename):
    os.system("tar -czf backup.tar.gz " + filename)

user_id = input("Enter user id: ")
print(search_user(user_id))

backup_file = input("Enter backup file name: ")
backup_database(backup_file)