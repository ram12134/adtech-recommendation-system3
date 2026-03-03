from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

DATA_FILE = "feedback_data.csv"


@app.get("/")
def home():
    return {"message":"Feedback Server Running"}


@app.post("/log_install")
def log_install(data: dict):

    df = pd.DataFrame([data])

    # Save to file
    if os.path.exists(DATA_FILE):

        df.to_csv(
            DATA_FILE,
            mode='a',
            header=False,
            index=False
        )

    else:

        df.to_csv(
            DATA_FILE,
            index=False
        )

    return {"status":"Saved"}