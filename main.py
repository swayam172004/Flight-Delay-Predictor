import streamlit as st
import joblib
import os
import numpy as np

# -----------------------------
# Load Models
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

clf_model = joblib.load(os.path.join(BASE_DIR, "model.joblib"))
reg_model = joblib.load(os.path.join(BASE_DIR, "regression_model.joblib"))

# -----------------------------
# UI
# -----------------------------
st.title("✈️ Flight Delay Prediction")

# =============================
# Delay Classification
# =============================
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

    features = np.array([[
        MONTH,
        DAY,
        SCHEDULED_ARRIVAL,
        ARRIVAL_TIME,
        ARRIVAL_DELAY,
        SCHEDULED_DEPARTURE,
        DEPARTURE_TIME,
        DEPARTURE_DELAY,
        DISTANCE,
        AIR_TIME
    ]])

    prediction = int(clf_model.predict(features)[0])

    if prediction == 1:
        st.error("✈️ Flight Delayed")
    else:
        st.success("✅ Flight On Time")


# =============================
# Delay Minutes Prediction
# =============================
st.header("Delay Minutes Prediction")

arr_delay = st.number_input("Arrival Delay", value=20.0, key="arr")
dep_delay = st.number_input("Departure Delay", value=15.0, key="dep")

if st.button("Predict Delay Minutes"):

    features = np.array([[arr_delay, dep_delay]])

    try:
        prediction = reg_model.predict(features)
        st.write("Prediction raw:", prediction)
        minutes = float(prediction[0])
        st.info(f"Delay: {round(minutes,2)} minutes")
    except Exception as e:
        st.error(str(e))


    st.info(f"🕒 Estimated Delay: {round(minutes, 2)} minutes")
