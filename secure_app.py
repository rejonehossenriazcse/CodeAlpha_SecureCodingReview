import os
import sqlite3
import hashlib
import socket

DATABASE_PASSWORD = os.getenv("DB_PASSWORD", "DefaultSafeSecretFallback")

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def check_host(ip, port=80):
    try:
        with socket.create_connection((ip, port), timeout=3):
            return True
    except (socket.timeout, socket.error):
        return False

def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

if __name__ == "__main__":
    print("Secure application initialized successfully.")