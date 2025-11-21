import streamlit as st
import numpy as np
import pickle

# Load  trained model
model = joblib.load("model.pkl")

st.title("Diabetes Prediction App")
st.write("Enter the values for the following :")

# Inputs for all independent variables
Pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
Glucose = st.number_input("Glucose", min_value=0)
BloodPressure = st.number_input("BloodPressure", min_value=0)
SkinThickness = st.number_input("SkinThickness", min_value=0)
Insulin = st.number_input("Insulin", min_value=0)
BMI = st.number_input("BMI", min_value=0.0, format="%.2f")
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", min_value=0.0, format="%.3f")
Age = st.number_input("Age", min_value=0, step=1)

# Convert inputs to model format
input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                        Insulin, BMI, DiabetesPedigreeFunction, Age]])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The model predicts: Diabetes Detected")
    else:
        st.success("The model predicts: No Diabetes")

