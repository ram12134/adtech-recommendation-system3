import sqlite3

conn = sqlite3.connect("ads.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS events")

conn.commit()
conn.close()

print("Old events table deleted")