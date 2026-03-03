import requests
import time
import random
from datetime import datetime

SERVER_URL = "http://127.0.0.1:8000"


# Convert window title → app category
def detect_category(window_title):

    title = window_title.lower()

    if "amazon" in title or "flipkart" in title:
        return "shopping"

    if "youtube" in title or "netflix" in title:
        return "entertainment"

    if "leetcode" in title or "github" in title:
        return "education"

    if "instagram" in title:
        return "social"

    return "other"


# Detect time of day
def get_time_of_day():

    hour = datetime.now().hour

    if hour < 12:
        return "morning"

    elif hour < 18:
        return "afternoon"

    else:
        return "evening"


# Send user behavior event
def send_event(window_title):

    event_data = {

        "user_id": "ram123",

        "window_title": window_title,

        "timestamp": time.time(),

        "device_type": "desktop",

        "country": "India",

        "app_category": detect_category(window_title),

        "time_of_day": get_time_of_day(),

        "connection": "wifi",

        "session_length": random.randint(30,600),

        "clicks": random.randint(0,10),

        "previous_installs": random.randint(0,5)

    }

    requests.post(
        SERVER_URL + "/event",
        json=event_data
    )


# Request ad from ML model
def request_ad(window_title):

    response = requests.post(
        SERVER_URL + "/serve_ad",
        json={"window_title": window_title}
    )

    print("\nServer Status:", response.status_code)
    print("Raw Response:", response.text)

    try:
        return response.json()
    except:
        return {"error": "Server returned invalid JSON"}

    response = requests.post(
        SERVER_URL + "/serve_ad",
        json=request_data
    )

    return response.json()


# Real-time simulation loop

while True:

    window = input("\nEnter active window title: ")

    send_event(window)

    ad = request_ad(window)

    print("\nSelected Ad:")
    print(ad)