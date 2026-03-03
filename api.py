from fastapi import FastAPI
import pandas as pd
import joblib
import random
import sqlite3
import json
import time
import datetime

app = FastAPI()


# =========================
# Load ML Model
# =========================

model = joblib.load("adtech_model.pkl")


# =========================
# Load Ads Inventory
# =========================

with open("ads.json") as f:
    ads_inventory = json.load(f)


# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():
    return {"message": "Full AdTech Engine Running"}


# =========================
# EVENT COLLECTION
# =========================

@app.post("/event")
def event(data: dict):

    title = data.get("window_title", "unknown")
    timestamp = time.time()

    conn = sqlite3.connect("ads.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        timestamp REAL
    )
    """)

    cursor.execute(
        "INSERT INTO events (title,timestamp) VALUES (?,?)",
        (title, timestamp)
    )

    conn.commit()
    conn.close()

    return {"status": "event saved"}


# =========================
# SERVE BEST AD
# =========================

@app.post("/serve_ad")
def serve_ad(data: dict):

    try:

        import random
        import datetime

        text = data.get("window_title","unknown")

        hour = datetime.datetime.now().hour

        features = pd.DataFrame([{

            "window_title": text,
            "hour": hour,
            "device_ram": random.choice([2,4,6,8]),
            "device_storage": random.choice([32,64,128,256])

        }])

        features = pd.get_dummies(features)

        model_columns = model.get_booster().feature_names

        for col in model_columns:
            if col not in features:
                features[col] = 0

        features = features[model_columns]

        prob = model.predict_proba(features)[0][1]
        pred = model.predict(features)[0]

        # REALISTIC AD SELECTION

        ads = list(ads_inventory.values())

        weights = []

        for ad in ads:
            weight = prob + random.uniform(0,0.5)
            weights.append(weight)

        selected_ad = random.choices(ads, weights=weights)[0]

        return {
            "selected_ad": selected_ad,
            "install_probability": float(prob)
        }

    except Exception as e:

        return {
            "error": str(e)
        }
# =========================
# AD RANKING ENGINE
# =========================

@app.post("/rank_ads")
def rank_ads(user_data: dict):

    networks = ["Facebook","Google","Unity","TikTok"]
    genres = ["Action","Puzzle","RPG","Casual"]

    ads = []

    for i in range(20):

        ad = user_data.copy()

        ad["ad_network"] = random.choice(networks)
        ad["game_genre"] = random.choice(genres)
        ad["campaign_type"] = random.choice(["Video","Banner"])

        bid = random.uniform(1,5)

        ad["bid"] = bid

        ads.append(ad)


    df = pd.DataFrame(ads)

    df_encoded = pd.get_dummies(df.drop("bid",axis=1))

    model_columns = model.get_booster().feature_names

    for col in model_columns:
        if col not in df_encoded:
            df_encoded[col] = 0

    df_encoded = df_encoded[model_columns]

    probs = model.predict_proba(df_encoded)[:,1]

    df["install_probability"] = probs
    df["expected_revenue"] = df["install_probability"] * df["bid"]

    best_ad = df.sort_values(
        "expected_revenue",
        ascending=False
    ).iloc[0]


    return {

        "best_ad_network": best_ad["ad_network"],
        "game_genre": best_ad["game_genre"],
        "campaign_type": best_ad["campaign_type"],

        "install_probability": float(best_ad["install_probability"]),
        "bid": float(best_ad["bid"]),
        "expected_revenue": float(best_ad["expected_revenue"])

    }


# =========================
# FEEDBACK LOOP
# =========================

@app.post("/feedback")
def feedback(data: dict):

    conn = sqlite3.connect("ads.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        network TEXT,
        genre TEXT,
        campaign TEXT,
        installed INTEGER
    )
    """)

    cursor.execute("""
    INSERT INTO feedback
    VALUES (?,?,?,?)
    """,
    (
        data["network"],
        data["genre"],
        data["campaign"],
        data["installed"]
    )
    )

    conn.commit()
    conn.close()

    return {"status":"feedback saved"}