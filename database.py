import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    income INTEGER,
    risk TEXT,
    strategy TEXT
)
""")

conn.commit()

def save_user(age, income, risk, strategy):
    cursor.execute(
        "INSERT INTO users (age, income, risk, strategy) VALUES (?, ?, ?, ?)",
        (age, income, risk, strategy)
    )
    conn.commit()

def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()