import os
import pickle
import streamlit as st

# Page config
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(os.path.join(working_dir, 'saved_models/diabetes_model.sav'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(working_dir, 'saved_models/heart_disease_model.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(working_dir, 'saved_models/parkinsons_model.sav'), 'rb'))

# Sidebar navigation
st.sidebar.title("🧑‍⚕️ Navigation")
menu = st.sidebar.radio("Go to", ["🏠 Home", "🩸 Diabetes Prediction", "❤️ Heart Disease Prediction", "🧠 Parkinson's Prediction"])

# Float conversion helper
def to_float(inputs):
    try:
        return [float(x) for x in inputs]
    except ValueError:
        st.error("Please enter all values as numbers.")
        return None

# ---------------------------------------------
# Home Page
if menu == "🏠 Home":
    st.title("🧠 Multiple Disease Prediction System")
    st.markdown("""
        ### Welcome to the AI Health Assistant App
        This web application helps predict the presence of three major diseases using Machine Learning models:
        - 🩸 **Diabetes**
        - ❤️ **Heart Disease**
        - 🧠 **Parkinson's Disease**

        ### 🔍 How it Works
        Each prediction model was trained on publicly available datasets using classification algorithms such as:
        - Logistic Regression
        - Random Forest
        - Support Vector Machines
        
        After entering patient data, the model instantly predicts whether the disease is likely present.

        ### 📂 Technologies Used
        - Python
        - Streamlit
        - Scikit-learn
        - Pandas & NumPy

        Use the sidebar to select a prediction type and try it out!
    """)

# ---------------------------------------------
# Diabetes Prediction
elif menu == "🩸 Diabetes Prediction":
    st.title("🩸 Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        SkinThickness = st.text_input("Skin Thickness")
        BMI = st.text_input("BMI")
    with col2:
        Glucose = st.text_input("Glucose Level")
        Insulin = st.text_input("Insulin")
        DPF = st.text_input("Diabetes Pedigree Function")
    with col3:
        BloodPressure = st.text_input("Blood Pressure")
        Age = st.text_input("Age")

    if st.button("Predict Diabetes"):
        inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]
        data = to_float(inputs)
        if data:
            prediction = diabetes_model.predict([data])
            st.success("✅ The person **is diabetic**." if prediction[0] == 1 else "❌ The person **is not diabetic**.")

# ---------------------------------------------
# Heart Disease Prediction
elif menu == "❤️ Heart Disease Prediction":
    st.title("❤️ Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
        trestbps = st.text_input("Resting Blood Pressure")
        restecg = st.text_input("Resting ECG (0-2)")
        oldpeak = st.text_input("Oldpeak")
        ca = st.text_input("Number of Major Vessels (0-3)")
    with col2:
        sex = st.text_input("Sex (1=Male, 0=Female)")
        chol = st.text_input("Cholesterol")
        thalach = st.text_input("Max Heart Rate")
        slope = st.text_input("Slope of ST Segment")
        thal = st.text_input("Thal (0=Normal, 1=Fixed, 2=Reversible)")
    with col3:
        cp = st.text_input("Chest Pain Type (0-3)")
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1/0)")
        exang = st.text_input("Exercise Induced Angina (1/0)")

    if st.button("Predict Heart Disease"):
        inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                  exang, oldpeak, slope, ca, thal]
        data = to_float(inputs)
        if data:
            prediction = heart_disease_model.predict([data])
            st.success("✅ The person **has heart disease**." if prediction[0] == 1 else "❌ The person **does not have heart disease**.")

# ---------------------------------------------
# Parkinson's Prediction
elif menu == "🧠 Parkinson's Prediction":
    st.title("🧠 Parkinson's Disease Prediction")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        RAP = st.text_input("MDVP:RAP")
        Shimmer = st.text_input("MDVP:Shimmer")
        APQ = st.text_input("MDVP:APQ")
        HNR = st.text_input("HNR")
        spread1 = st.text_input("Spread1")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        PPQ = st.text_input("MDVP:PPQ")
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
        DDA = st.text_input("Shimmer:DDA")
        RPDE = st.text_input("RPDE")
        spread2 = st.text_input("Spread2")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
        DDP = st.text_input("Jitter:DDP")
        APQ3 = st.text_input("Shimmer:APQ3")
        NHR = st.text_input("NHR")
        DFA = st.text_input("DFA")
        D2 = st.text_input("D2")

    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
        APQ5 = st.text_input("Shimmer:APQ5")
        PPE = st.text_input("PPE")

    if st.button("Predict Parkinson's"):
        inputs = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                  Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
                  RPDE, DFA, spread1, spread2, D2, PPE]
        data = to_float(inputs)
        if data:
            prediction = parkinsons_model.predict([data])
            st.success("✅ The person **has Parkinson's disease**." if prediction[0] == 1 else "❌ The person **does not have Parkinson's disease**.")
