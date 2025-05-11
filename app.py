import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import os

model_path = 'model.h5'

model = load_model(model_path)
st.success("Model loaded successfully!")

st.title("🔎 Fraud Detection Predictor (30 Features, Auto-Fill)")

st.header("Enter 30 Features:")

features = []
for i in range(30):
    val = st.number_input(f"Feature {i+1}", value=np.round(np.random.uniform(-1, 1), 4))
    features.append(val)

if st.button("Predict"):
    features_array = np.array([features])  
    prediction = model.predict(features_array)

    result = prediction[0][0]
    st.subheader("📝 Prediction:")
    st.write(f"Fraud Probability Score: {result:.4f}")

    if result > 0.5:
        st.error(f"⚠️ Fraud Detected! (Score: {result:.2f})")
    else:
        st.success(f"✅ Transaction Safe (Score: {result:.2f})")
