import streamlit as st
import requests

st.title("Obesity Prediction App")
st.write(
    "This app predicts your obesity level based on your personal and lifestyle information.\n"
    "Fill in the details below and get an instant prediction of your obesity category.\n"
    "Developed by Syalista Galuh Nadira"
)

st.subheader("Input Your Data")

# Form input
with st.form("prediction_form"):
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", min_value=0, max_value=120)
    Height = st.number_input("Height (m)", min_value=0.5, max_value=2.0)
    Weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0)
    family_history_with_overweight = st.selectbox("Family history with overweight", ["no", "yes"])
    FAVC = st.selectbox("Frequent high caloric food consumption (FAVC)", ["no", "yes"])
    FCVC = st.number_input("Vegetable consumption frequency (FCVC)", min_value=0.0, max_value=3.0)
    NCP = st.number_input("Number of main meals (NCP)", min_value=1.0, max_value=5.0)
    CAEC = st.selectbox("Consumption of food between meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("Do you smoke?", ["no", "yes"])
    CH2O = st.number_input("Daily water intake (CH2O)", min_value=1.0, max_value=5.0)
    SCC = st.selectbox("Monitor calories consumption?", ["no", "yes"])
    FAF = st.number_input("Physical activity frequency (FAF)", min_value=0.0, max_value=5.0)
    TUE = st.number_input("Time using technology devices (TUE)", min_value=0.0, max_value=24.0)
    CALC = st.selectbox("Alcohol consumption", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("Transportation used", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])
    submit = st.form_submit_button("Submit")

if submit:
    payload = {
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": FAVC,
        "FCVC": FCVC,
        "NCP": NCP,
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": CH2O,
        "SCC": SCC,
        "FAF": FAF,
        "TUE": TUE,
        "CALC": CALC,
        "MTRANS": MTRANS
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        response.raise_for_status()
        result = response.json()
        st.success(f"Your predicted obesity category is: {result['prediction']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
