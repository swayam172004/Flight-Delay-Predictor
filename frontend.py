import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.title("✈️ Flight Delay Prediction")

# -----------------------------
# Delay Classification
# -----------------------------
st.header("Delay Status Prediction")

MONTH = st.number_input("Month", 1, 12, 6)
DAY = st.number_input("Day", 1, 31, 15)
SCHEDULED_ARRIVAL = st.number_input("Scheduled Arrival", 0, 2359, 1400)
ARRIVAL_TIME = st.number_input("Actual Arrival", 0, 2359, 1420)
ARRIVAL_DELAY = st.number_input("Arrival Delay (min)", value=20.0)
SCHEDULED_DEPARTURE = st.number_input("Scheduled Departure", 0, 2359, 1200)
DEPARTURE_TIME = st.number_input("Actual Departure", 0, 2359, 1215)
DEPARTURE_DELAY = st.number_input("Departure Delay (min)", value=15.0)
DISTANCE = st.number_input("Distance (miles)", value=800.0)
AIR_TIME = st.number_input("Air Time (min)", value=120.0)

if st.button("Predict Delay Status"):
    payload = {
        "MONTH": MONTH,
        "DAY": DAY,
        "SCHEDULED_ARRIVAL": SCHEDULED_ARRIVAL,
        "ARRIVAL_TIME": ARRIVAL_TIME,
        "ARRIVAL_DELAY": ARRIVAL_DELAY,
        "SCHEDULED_DEPARTURE": SCHEDULED_DEPARTURE,
        "DEPARTURE_TIME": DEPARTURE_TIME,
        "DEPARTURE_DELAY": DEPARTURE_DELAY,
        "DISTANCE": DISTANCE,
        "AIR_TIME": AIR_TIME
    }

    try:
        response = requests.post(f"{FASTAPI_URL}/predict_delay", json=payload, timeout=5)
        result = response.json()
        st.success("Delayed" if result["delay"] else "On Time")
    except Exception:
        st.error("❌ Backend not reachable")

# -----------------------------
# Delay Minutes
# -----------------------------
st.header("Delay Minutes Prediction")

arr_delay = st.number_input("Arrival Delay", value=20.0)
dep_delay = st.number_input("Departure Delay", value=15.0)

if st.button("Predict Delay Minutes"):
    payload = {
        "ARRIVAL_DELAY": arr_delay,
        "DEPARTURE_DELAY": dep_delay
    }

    try:
        response = requests.post(f"{FASTAPI_URL}/predict_delay_minutes", json=payload, timeout=5)
        result = response.json()
        st.success(f"{result['delay_minutes']} minutes")
    except Exception:
        st.error("❌ Backend not reachable")
