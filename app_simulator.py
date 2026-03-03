import requests
import random
import time

URL = "http://127.0.0.1:8000/rank_ads"

for i in range(10):

    # Simulated user data
    user = {
        "country":"India",
        "device":"Android",
        "hour": random.randint(0,23),
        "day": random.randint(1,7),
        "age": random.randint(18,40),
        "session_time": random.randint(50,400),
        "clicks": random.randint(0,5),
        "impressions": random.randint(1,10),
        "previous_installs": random.randint(0,3),
        "spend": round(random.uniform(0.5,3),2),
        "wifi": random.randint(0,1),
        "battery": random.randint(20,100),
        "screen_time": random.randint(100,600),
        "level": random.randint(1,10),
        "in_app_purchase": random.randint(0,1)
    }

    # Call ranking server
    response = requests.post(URL, json=user)

    result = response.json()   # ← THIS FIXES ERROR

    print(result)


    # Simulate install
    install = random.random() < result["install_probability"]


    # Send feedback
    requests.post(
        "http://127.0.0.1:8000/feedback",
        json={
            "install": int(install)
        }
    )

    time.sleep(1)