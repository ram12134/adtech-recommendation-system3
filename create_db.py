import sqlite3

conn = sqlite3.connect("ads.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (

id INTEGER PRIMARY KEY AUTOINCREMENT,

country TEXT,
device TEXT,
ad_network TEXT,
game_genre TEXT,
campaign_type TEXT,

install_probability REAL,
bid REAL,
expected_revenue REAL,

installed INTEGER

)
""")

conn.commit()

conn.close()

print("Database Created Successfully")


import sqlite3

conn = sqlite3.connect("ads.db")
cursor = conn.cursor()

# Create events table
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    user_id TEXT,
    window_title TEXT,
    timestamp REAL
)
""")

conn.commit()
conn.close()

print("Database initialized successfully.")