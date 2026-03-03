from fastapi import FastAPI
import pandas as pd
import joblib
import random

app = FastAPI()

# Load trained model
model = joblib.load("adtech_model.pkl")

# Model feature columns
model_columns = model.get_booster().feature_names


@app.get("/")
def home():
    return {"message": "AdTech Ranking + Auction Server Running"}


@app.post("/rank_ads")
def rank_ads(user_data: dict):

    # Generate candidate ads
    ads = []

    networks = ["Facebook","Google","Unity","TikTok"]
    genres = ["Action","Puzzle","RPG","Casual"]
    campaigns = ["Video","Banner"]

    for i in range(30):

        ad = user_data.copy()

        ad["ad_network"] = random.choice(networks)
        ad["game_genre"] = random.choice(genres)
        ad["campaign_type"] = random.choice(campaigns)

        # Bid price (Advertiser paying)
        ad["bid"] = random.uniform(0.5,5)

        ads.append(ad)


    # Convert to dataframe
    df = pd.DataFrame(ads)

    # Remove bid before prediction
    df_model = df.drop(["bid"],axis=1)

    # One-hot encoding
    df_encoded = pd.get_dummies(df_model)

    # Align features
    for col in model_columns:
        if col not in df_encoded:
            df_encoded[col] = 0

    df_encoded = df_encoded[model_columns]


    # Predict install probabilities
    probs = model.predict_proba(df_encoded)[:,1]

    df["install_probability"] = probs


    # Revenue Formula (Industry Standard)
    df["expected_revenue"] = df["install_probability"] * df["bid"]


    # Select best ad
    best_ad = df.sort_values(
        "expected_revenue",
        ascending=False
    ).iloc[0]


    return {

        "best_ad_network": best_ad["ad_network"],

        "game_genre": best_ad["game_genre"],

        "campaign_type": best_ad["campaign_type"],

        "install_probability":
        float(best_ad["install_probability"]),

        "bid":
        float(best_ad["bid"]),

        "expected_revenue":
        float(best_ad["expected_revenue"])

    }