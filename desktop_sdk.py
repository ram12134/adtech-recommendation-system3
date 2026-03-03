import time
import requests
import pygetwindow as gw

SERVER_URL = "http://127.0.0.1:8000/event"

def get_active_window():

    try:
        window = gw.getActiveWindow()
        return window.title
    except:
        return "Unknown"


while True:

    title = get_active_window()

    data = {
        "user_id": "ram123",
        "window_title": title,
        "timestamp": time.time()
    }

    requests.post(SERVER_URL, json=data)

    time.sleep(5)
    response = requests.post(
"http://127.0.0.1:8000/serve_ad",
json={"window_title":title}
)

print("Ad:",response.json())