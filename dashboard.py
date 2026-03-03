import sqlite3

# Connect to the database
conn = sqlite3.connect("ads.db")
cursor = conn.cursor()

# Get total ads
cursor.execute("SELECT COUNT(*) FROM feedback")
total_ads = cursor.fetchone()[0]

# Get total installs
cursor.execute("SELECT COUNT(*) FROM feedback WHERE installed=1")
installs = cursor.fetchone()[0]

# Calculate install rate safely
install_rate = (installs / total_ads * 100) if total_ads != 0 else 0

# Calculate pending installs
pending_installs = total_ads - installs

# Print a clean dashboard
print("\n--- Ad Dashboard ---")
print(f"Total Ads       : {total_ads}")
print(f"Installs        : {installs}")
print(f"Install Rate    : {install_rate:.2f}%")
print(f"Pending Installs: {pending_installs}")
print("--------------------\n")

# Close the connection
conn.close()
import sqlite3

conn = sqlite3.connect("ads.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events(
user_id TEXT,
window_title TEXT,
timestamp REAL
)
""")

conn.commit()
conn.close()