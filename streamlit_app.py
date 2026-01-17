import streamlit as st
import requests

st.set_page_config(
    page_title="Student Performance Predictor",
    layout="centered"
)

st.title("Student Performance Predictor")
st.write("Predict whether a student will **Pass or Fail** using ML")

study_hours = st.number_input("Study Hours", min_value=0.0, max_value=15.0, step=0.1)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, step=1.0)
previous_score = st.number_input("Previous Score", min_value=0.0, max_value=100.0, step=1.0)

if st.button("Predict"):
    payload = {
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,  
            timeout=5      
        )

        result = response.json()
        st.success(f"Prediction: **{result['prediction']}**")

   
    except Exception as e:
        st.error(f"API Error: {e}")
         
