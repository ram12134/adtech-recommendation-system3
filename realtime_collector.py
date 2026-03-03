import time
import requests
import pygetwindow as gw

EVENT_URL = "http://127.0.0.1:8000/event"
AD_URL = "http://127.0.0.1:8000/serve_ad"

last = ""

while True:

    try:

        win = gw.getActiveWindow()

        if win:

            title = win.title

            if title != last:

                data = {
                    "window_title": title
                }

                # Send Event
                r1 = requests.post(EVENT_URL, json=data)

                print("\nEvent Sent:", title)
                print("Event:", r1.text)

                # Get Ad
                r2 = requests.post(AD_URL, json=data)

                print("Selected Ad:")
                print(r2.json())

                last = title

        time.sleep(2)

    except Exception as e:
        print(e)