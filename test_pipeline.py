import sqlite3
import random

# Connect to database
conn = sqlite3.connect("ads.db")
cursor = conn.cursor()

# Fix missing column if needed
try:
    cursor.execute("ALTER TABLE feedback ADD COLUMN ad_name TEXT DEFAULT 'Ad'")
except sqlite3.OperationalError:
    # Column already exists
    pass

# Step 1: Simulate generating ads
ads_to_generate = 5
for i in range(ads_to_generate):
    cursor.execute("INSERT INTO feedback (ad_name, installed) VALUES (?, ?)",
                   (f"Ad {i+1}", 0))

conn.commit()
print(f"{ads_to_generate} ads generated and added to DB.")

# Step 2: Simulate user interactions (random installs)
cursor.execute("SELECT id FROM feedback")
all_ads = cursor.fetchall()
for ad in all_ads:
    if random.choice([True, False]):
        cursor.execute("UPDATE feedback SET installed=1 WHERE id=?", (ad[0],))

conn.commit()
print("Random installs updated in DB.")

# Step 3: Run your dashboard code
cursor.execute("SELECT COUNT(*) FROM feedback")
total_ads = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM feedback WHERE installed=1")
installs = cursor.fetchone()[0]

install_rate = (installs / total_ads * 100) if total_ads != 0 else 0
pending_installs = total_ads - installs

print("\n--- Pipeline Test Dashboard ---")
print(f"Total Ads       : {total_ads}")
print(f"Installs        : {installs}")
print(f"Install Rate    : {install_rate:.2f}%")
print(f"Pending Installs: {pending_installs}")
print("--------------------\n")

# Close connection
conn.close()