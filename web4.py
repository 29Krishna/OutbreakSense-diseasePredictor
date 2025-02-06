import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='OutbreakSense - Predict Diseases with Intelligent insights', layout='wide', page_icon='🩺')

# Load trained models
model_path = os.path.join(os.getcwd(), "saved-models", "diabetes_model.sav")
diabetes_model = pickle.load(open(model_path, 'rb'))
model_path = os.path.join(os.getcwd(), "saved-models", "parkinsons_model.sav")
parkinsons_model = pickle.load(open(model_path, 'rb'))
model_path = os.path.join(os.getcwd(), "saved-models", "hearts_model.sav")
hearts_model = pickle.load(open(model_path, 'rb'))


with st.sidebar:
    st.title("🩺 OutbreakSense")
    st.info("Select a disease prediction model or predict an outbreak in your area.")

    selected = option_menu(
        "Prediction Options",
        ["Disease Prediction", "Outbreak Prediction"],
        menu_icon="hospital-fill",
        icons=["stethoscope", "exclamation-triangle"],
        default_index=0
    )

    
    disease_selected = None  
    if selected == "Disease Prediction":
        disease_selected = option_menu(
            "Select Disease",
            ["Diabetes", "Heart Disease", "Parkinsons"],
            menu_icon="hospital-fill",
            icons=["activity", "heart", "person"],
            default_index=0
        )


# ✅ Diabetes Prediction
def diabetes_prediction():
    st.title("🩸 Diabetes Prediction using ML")
    with st.form("diabetes_form"):
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
            Glucose = st.number_input("Glucose Level", min_value=0.0)
            BloodPressure = st.number_input("Blood Pressure", min_value=0.0)
            SkinThickness = st.number_input("Skin Thickness", min_value=0.0)
        with col2:
            Insulin = st.number_input("Insulin Level", min_value=0.0)
            BMI = st.number_input("Body Mass Index (BMI)", min_value=0.0)
            DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0)
            Age = st.number_input("Age", min_value=1, step=1)

        submitted = st.form_submit_button("Predict Diabetes")
        if submitted:
            with st.spinner("Analyzing your inputs..."):
                user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
                diab_prediction = diabetes_model.predict([user_input])
                result = "You are Diabetic 😔" if diab_prediction[0] == 1 else "You are not Diabetic 😊"
                st.success(result)

# ✅ Heart Disease Prediction
def heart_disease_prediction():
    st.title("❤️ Heart Disease Prediction using ML")
    with st.form("heart_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=1, step=1)
            sex = st.radio("Gender", ["Male", "Female"])
            cp = st.number_input("Chest Pain Type (cp)", min_value=0, max_value=3)
            trestbps = st.number_input("Resting Blood Pressure", min_value=0)
            chol = st.number_input("Cholesterol Level", min_value=0)
        with col2:
            fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
            restecg = st.number_input("Resting ECG Results", min_value=0, max_value=2)
            thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0)
            exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
            oldpeak = st.number_input("ST Depression", min_value=0.0)

        submitted = st.form_submit_button("Predict Heart Disease")
        if submitted:
            with st.spinner("Processing your inputs..."):
                user_input = [age, 1 if sex == "Male" else 0, cp, trestbps, chol, 1 if fbs == "Yes" else 0, restecg, thalach, 1 if exang == "Yes" else 0, oldpeak]
                hearts_prediction = hearts_model.predict([user_input])
                result = "You may have Heart Disease 😔" if hearts_prediction[0] == 1 else "Your heart is healthy 😊"
                st.success(result)

# ✅ Parkinson’s Prediction
def parkinsons_prediction():
    st.title("🧠 Parkinson’s Disease Prediction using ML")
    with st.form("parkinsons_form"):
        col1, col2 = st.columns(2)
        with col1:
            MDVPFo = st.number_input("MDVP:Fo(Hz)", min_value=0.0)
            MDVPFhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0)
            MDVPFlo = st.number_input("MDVP:Flo(Hz)", min_value=0.0)
            MDVPJitter = st.number_input("MDVP:Jitter(%)", min_value=0.0)
        with col2:
            MDVPJitterAbs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0)
            MDVPRAP = st.number_input("MDVP:RAP", min_value=0.0)
            MDVPPPQ = st.number_input("MDVP:PPQ", min_value=0.0)
            JitterDDP = st.number_input("Jitter:DDP", min_value=0.0)

        submitted = st.form_submit_button("Predict Parkinson's")
        if submitted:
            with st.spinner("Analyzing your voice parameters..."):
                user_input = [MDVPFo, MDVPFhi, MDVPFlo, MDVPJitter, MDVPJitterAbs, MDVPRAP, MDVPPPQ, JitterDDP]
                park_prediction = parkinsons_model.predict([user_input])
                result = "You may have Parkinson’s Disease 😔" if park_prediction[0] == 1 else "No signs of Parkinson’s 😊"
                st.success(result)

# ✅ Outbreak Prediction
def outbreak_prediction():
    st.title("Outbreak Prediction")
    st.markdown("**Note:** This model demonstrates a simple approach to outbreak risk estimation.")
    
    with st.form("outbreak_form"):
        region = st.text_input("Enter Region Name")
        population = st.number_input("Population in the Area", min_value=1, step=1, value=1000)
        current_cases = st.number_input("Current Reported Cases", min_value=0, step=1, value=0)
        threshold = st.number_input("Outbreak Threshold (cases per 1000 people)", min_value=0.0, step=0.1, value=1.0)

        submitted = st.form_submit_button("Predict Outbreak")
        if submitted:
            cases_per_1000 = (current_cases / population) * 1000
            st.write(f"**Cases per 1000 people:** {cases_per_1000:.2f}")
            if cases_per_1000 > threshold:
                st.error(f"🚨 Outbreak Detected in {region}!")
            else:
                st.success(f"No outbreak detected in {region}.")


if selected == "Disease Prediction" and disease_selected:
    if disease_selected == "Diabetes":
        diabetes_prediction()
    elif disease_selected == "Heart Disease":
        heart_disease_prediction()
    elif disease_selected == "Parkinsons":
        parkinsons_prediction()
elif selected == "Outbreak Prediction":
    outbreak_prediction()
