import streamlit as st
import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_models():
    clf = joblib.load(os.path.join(BASE_DIR, "model.joblib"))
    reg = joblib.load(os.path.join(BASE_DIR, "regression_model.joblib"))
    return clf, reg

clf_model, reg_model = load_models()

if st.button("Predict"):
    features = np.array([[MONTH, DAY, SCHEDULED_ARRIVAL, ARRIVAL_TIME,
                          ARRIVAL_DELAY, SCHEDULED_DEPARTURE, DEPARTURE_TIME,
                          DEPARTURE_DELAY, DISTANCE, AIR_TIME]])

    delay = int(clf_model.predict(features)[0])
    st.success(f"Delay: {delay}")

if st.button("Predict Delay Minutes"):
    minutes = reg_model.predict([[ARRIVAL_DELAY, DEPARTURE_DELAY]])
    st.success(f"Delay Minutes: {round(float(minutes[0]), 2)}")
