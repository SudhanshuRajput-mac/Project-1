import streamlit as st
import pandas as pd
import joblib
import numpy as np
# Load model
model = joblib.load('model.pkl')

st.title("Multiple Linear Regression Predictor")

# Input features
feature1 = st.number_input("Enter Hours Studied:")
feature2 = st.number_input("Enter Previous Scores:")
feature3 = st.number_input("Enter Extracurricular Activities:")
feature4 = st.number_input("Enter Sleep Hours:")
feature5 = st.number_input("Enter Sample Question Papers Practiced : ")

# Predict button
if st.button("Predict"):
    data = np.array([[feature1, feature2 , feature3,feature4,feature5]])
    prediction = model.predict(data)
    st.success(f"Predicted Value: {prediction[0]}")
