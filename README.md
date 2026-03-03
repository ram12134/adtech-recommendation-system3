AdTech Recommendation System

This project is a simple ad recommendation system that selects ads based on user activity. The idea was to simulate how adtech companies decide which ad to show to a user in real time.

The system collects user activity (like search or page title), sends it to an API, and the backend selects the best ad using a machine learning model and ranking logic.

I built this project to understand how real ad networks work — event tracking, ranking ads, feedback loops, and real-time serving.

How It Works

Basic flow:

User Activity → API → Ranking → ML Model → Best Ad → Feedback → Dashboard

Example:

User searches "Amazon shoes"

Event is sent to API

Model predicts interest

Best ad is selected

Feedback stored

Files
Core Files

api.py
Main FastAPI server that receives events and serves ads.

ranking_server.py
Contains logic to rank and select ads.

feature_engineering.py
Converts user events into model features.

training.py
Trains the machine learning model.

ads.json
List of available ads.

Simulation Files

send_event.py
Simulates user activity.

Example input:

Amazon shoes
YouTube
Laptop
Data & Storage

database.py
Handles database connection.

ads.db
Stores events and feedback.

Dashboard

dashboard.py

Shows basic statistics like:

Number of events

Feedback count

Ads served

How To Run
1 Install Requirements
pip install fastapi uvicorn pandas scikit-learn numpy
2 Train Model
python training.py

This creates:

adtech_model.pkl
training_columns.pkl
3 Start API
uvicorn api:app --reload

Server runs on:

http://127.0.0.1:8000
4 Send Events
python send_event.py

Type something like:

Amazon shoes

The system will return a selected ad.

5 Run Dashboard
python dashboard.py

Shows stored statistics.

What I Learned

Real-time event tracking

API based ad serving

Feature engineering

Machine learning integration

Feedback based ranking

Debugging API issues

Hardest Part

The hardest part was connecting the event tracking with the ranking system and making the API return ads correctly in real time. Debugging server responses and fixing data format issues took the most time.

Future Improvements

Real-time browser tracking

Better ranking model

Online learning

Deploy API online

Author

Ram Kuchiya
