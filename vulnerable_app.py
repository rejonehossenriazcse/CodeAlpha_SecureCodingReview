import os
import sqlite3
import hashlib

DATABASE_PASSWORD = "SuperSecretAdminPassword123!"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

def check_host(ip):
    os.system("ping -c 1 " + ip)

def make_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == "__main__":
    print("Vulnerable application ready.")