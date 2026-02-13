import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Flight Delay Predictor",
    page_icon="✈️",
    layout="wide"
)

# -------------------------------
# Load Models
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_models():
    clf_path = os.path.join(BASE_DIR, "model.joblib")
    reg_path = os.path.join(BASE_DIR, "regression_model.joblib")

    clf = joblib.load(clf_path)
    reg = joblib.load(reg_path)

    return clf, reg
clf_model, reg_model = load_models()

# -------------------------------
# Header Section
# -------------------------------
st.title("✈️ Flight Delay Predictor")
st.markdown("Predict flight delay status and estimated delay time using Machine Learning.")

st.divider()

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📌 Enter Flight Details")

col1, col2, col3 = st.columns(3)

with col1:
    airline = st.selectbox("Airline", ["Airline A", "Airline B", "Airline C"])
    source = st.selectbox("Source Airport", ["Delhi", "Mumbai", "Chennai"])

with col2:
    destination = st.selectbox("Destination Airport", ["Bangalore", "Kolkata", "Hyderabad"])
    distance = st.number_input("Distance (km)", min_value=0)

with col3:
    departure_hour = st.slider("Departure Hour", 0, 23)
    day_of_week = st.selectbox("Day of Week", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

st.divider()

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("🔍 Predict Delay"):

    with st.spinner("Analyzing flight data..."):

        # Prepare DataFrame (must match training features)
        features = pd.DataFrame([{
            "Airline": airline,
            "Source": source,
            "Destination": destination,
            "Distance": distance,
            "Departure_Hour": departure_hour,
            "Day_of_Week": day_of_week
        }])

        try:
            # Classification
            clf_prediction = clf_model.predict(features)
            delay_status = int(np.ravel(clf_prediction)[0])

            # Regression
            reg_prediction = reg_model.predict(features)
            delay_minutes = float(np.ravel(reg_prediction)[0])

            st.success("Prediction Complete ✅")

            col1, col2 = st.columns(2)

            with col1:
                if delay_status == 1:
                    st.error("⚠️ Flight is likely to be Delayed")
                else:
                    st.success("✅ Flight is likely to be On-Time")

            with col2:
                st.info(f"🕒 Estimated Delay: {round(delay_minutes, 2)} minutes")

        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

st.divider()

# -------------------------------
# Footer
# -------------------------------
st.caption("Built with ❤️ using XGBoost & Streamlit")
