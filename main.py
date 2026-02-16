import streamlit as st
import joblib
import os
import numpy as np

# =========================================================
# Page Config
# =========================================================
st.set_page_config(
    page_title="Flight Delay Predictor",
    page_icon="✈️",
    layout="wide"
)

# =========================================================
# Load Models (Production Safe)
# =========================================================
@st.cache_resource
def load_models():
    try:
        clf = joblib.load("model.joblib")
        reg = joblib.load("regression_model.joblib")
        return clf, reg
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        st.stop()

clf_model, reg_model = load_models()

# =========================================================
# Header Section
# =========================================================
st.title("✈️ Flight Delay Prediction System")
st.markdown(
    """
    Machine Learning–powered system to:
    - Predict **Flight Delay Status**
    - Estimate **Delay Duration (Minutes)**
    """
)

st.divider()

# =========================================================
# Sidebar Input Panel
# =========================================================
st.sidebar.header("📋 Flight Input Parameters")

MONTH = st.sidebar.number_input("Month", 1, 12, 6)
DAY = st.sidebar.number_input("Day", 1, 31, 15)

SCHEDULED_DEPARTURE = st.sidebar.number_input("Scheduled Departure (HHMM)", 0, 2359, 1200)
DEPARTURE_TIME = st.sidebar.number_input("Actual Departure (HHMM)", 0, 2359, 1215)
DEPARTURE_DELAY = st.sidebar.number_input("Departure Delay (min)", value=15.0)

SCHEDULED_ARRIVAL = st.sidebar.number_input("Scheduled Arrival (HHMM)", 0, 2359, 1400)
ARRIVAL_TIME = st.sidebar.number_input("Actual Arrival (HHMM)", 0, 2359, 1420)
ARRIVAL_DELAY = st.sidebar.number_input("Arrival Delay (min)", value=20.0)

DISTANCE = st.sidebar.number_input("Distance (miles)", value=800.0)
AIR_TIME = st.sidebar.number_input("Air Time (min)", value=120.0)

st.divider()

# =========================================================
# Tabs for Clean Separation
# =========================================================
tab1, tab2 = st.tabs(["🛫 Delay Status", "🕒 Delay Minutes"])

# =========================================================
# TAB 1 — Classification
# =========================================================
with tab1:

    st.subheader("Predict Flight Delay Status")

    if st.button("🔍 Predict Delay Status", use_container_width=True):

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

        try:
            prediction = int(clf_model.predict(features)[0])

            st.success("Prediction Complete ✅")

            if prediction == 1:
                st.error("⚠️ Flight is likely to be **Delayed**")
            else:
                st.success("✅ Flight is likely to be **On Time**")

        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

# =========================================================
# TAB 2 — Regression
# =========================================================
with tab2:

    st.subheader("Predict Delay Duration (Minutes)")

    if st.button("🕒 Predict Delay Minutes", use_container_width=True):

        features = np.array([[ARRIVAL_DELAY, DEPARTURE_DELAY]])

        try:
            minutes = float(reg_model.predict(features).flatten()[0])

            st.success("Prediction Complete ✅")
            st.info(f"Estimated Delay: **{round(minutes, 2)} minutes**")

        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

# =========================================================
# Footer
# =========================================================
st.divider()
