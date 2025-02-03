import os
import pickle #pre trained model loading
import streamlit as st #web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='OutbreakSense-Predict outbreaks with intelligent insights', layout='wide', page_icon='doctor')

diabetes_model = pickle.load(open(r"saved-models\diabetes_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"saved-models\parkinsons_model.sav",'rb'))
hearts_model = pickle.load(open(r"saved-models\hearts_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('OutbreakSense', ['Diabetes','Heart Disease','Parkinsons'], menu_icon='hospital-fill',icons=['activity','heart','person'], default_index=0)

#diabetes
if selected == 'Diabetes':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Enter No. of Pregnancies')
    with col2:
        Glucose = st.text_input('Enter Glucose level')
    with col3:
        BloodPressure = st.text_input('Enter your Blood Pressure')
    with col1:
        SkinThickness = st.text_input('Enter Skin Thickness')
    with col2:
        Insulin = st.text_input('Enter Insulin')
    with col3:
        BMI = st.text_input('Enter your BMI')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Enter Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Enter age')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'You are Diabetic😔'
        else:
            diab_diagnosis = 'You are not Diabetic 😊'
    st.success(diab_diagnosis)


#hearts disease
if selected == 'Heart Disease':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Enter Age')
    with col2:
        sex = st.text_input('Enter your gender')
    with col3:
        cp = st.text_input('Enter cp value')
    with col1:
        trestbps = st.text_input('Enter trestbps value')
    with col2:
        chol = st.text_input('Enter cholestrol value')
    with col3:
        fbs = st.text_input('Enter fbs value')
    with col1:
        restecg = st.text_input('Enter restecg value')
    with col2:
        thalach = st.text_input('Enter thalach value')
    with col3:
        exang = st.text_input('Enter exang value')
    with col1:
        oldpeak = st.text_input('Enter oldpeak value')
    with col2:
        slope = st.text_input('Enter slope value')
    with col3:
        ca = st.text_input('Enter ca value')
    with col1:
        thal = st.text_input('Enter thal value')

    hearts_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        hearts_prediction = hearts_model.predict([user_input])
        if hearts_prediction[0] == 1:
            hearts_diagnosis = "You may have a heart's disease😔"
        else:
            hearts_diagnosis = "You do not have a heart's disease😊"
    st.success(hearts_diagnosis)


#parkinsons
if selected == 'Parkinsons':
    st.title('Parkinsons Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        MDVPFo = st.text_input('MDVP:Fo(Hz):')
    with col2:
        MDVPFhi = st.text_input('MDVP:Fhi(Hz):')
    with col3:
        MDVPFlo = st.text_input('MDVP:Flo(Hz):')
    with col1:
        MDVPJitter = st.text_input('MDVP:Jitter(%):')
    with col2:
        MDVPJitterAbs = st.text_input('MDVP:Jitter(Abs):')
    with col3:
        MDVPRAP = st.text_input('MDVP:RAP:')
    with col1:
        MDVPPPQ = st.text_input('MDVP:PPQ:')
    with col2:
        JitterDDP = st.text_input('Jitter:DDP:')
    with col3:
        MDVPShimmer = st.text_input('MDVP:Shimmer:')
    with col1:
        MDVPShimmerdb = st.text_input('MDVP:Shimmer(dB):')
    with col2:
        ShimmerAPQ3 = st.text_input('Shimmer:APQ3:')
    with col3:
        ShimmerAPQ5 = st.text_input('Shimmer:APQ5:')
    with col1:
        MDVPAPQ = st.text_input('MDVP:APQ:')
    with col2:
        ShimmerDDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR:')
    with col1:
        HNR = st.text_input('HNR:')
    with col2:
        RPDE = st.text_input('RPDE:')
    with col3:
        DFA = st.text_input('DFA:')
    with col1:
        spread1 = st.text_input('spread1:')
    with col2:
        spread2 = st.text_input('spread2:')
    with col3:
        D2 = st.text_input('D2:')
    with col1:
        PPE = st.text_input('PPE:')

    park_diagnosis = ''
    if st.button('Parkinsons Test Result'):
        user_input = [MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdb,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input = [float(x) for x in user_input]
        park_prediction = parkinsons_model.predict([user_input])
        if park_prediction[0] == 1:
            park_diagnosis = 'You have Parkinsons Disease 😔'
        else:
            park_diagnosis = 'You do not have Parkinsons Disease 😊'
    st.success(park_diagnosis)
