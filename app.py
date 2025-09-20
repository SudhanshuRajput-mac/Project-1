# import streamlit as st
# import pandas as pd
# import joblib

# # Load model
# model = joblib.load('model.pkl')

# st.title("Multiple Linear Regression Predictor")

# # Input features
# feature1 = st.number_input("Enter Hours Studied:")
# feature2 = st.number_input("Enter Previous Scores:")
# feature3 = st.number_input("Enter Extracurricular Activities:")
# feature4 = st.number_input("Enter Sleep Hours:")
# feature5 = st.number_input("Enter Sample Question Papers Practiced : ")

# # Predict button
# if st.button("Predict"):
#     data = pd.DataFrame([[feature1, feature2 , feature3,feature4,feature5]], columns=['Feature1', 'Feature2' , 'Feature3' , 'Feature4','Feature5'])
#     prediction = model.predict(data)
#     st.success(f"Predicted Value: {prediction[0]}")

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

st.title("Multiple Linear Regression Predictor")

# Input features with defaults
feature1 = st.number_input("Enter Hours Studied:", value=0.0)
feature2 = st.number_input("Enter Previous Scores:", value=0.0)
feature3 = st.number_input("Enter Extracurricular Activities:", value=0.0)
feature4 = st.number_input("Enter Sleep Hours:", value=0.0)
feature5 = st.number_input("Enter Sample Question Papers Practiced : ", value=0.0)

# Predict button
if st.button("Predict"):
    # Optional: Add explicit validation
    if None in [feature1, feature2, feature3, feature4, feature5]:
        st.error("Please enter valid numbers for all fields.")
    else:
        data = pd.DataFrame([[feature1, feature2, feature3, feature4, feature5]], columns=['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])
        prediction = model.predict(data)
        st.success(f"Predicted Value: {prediction[0]}")
