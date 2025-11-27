import pandas as pd
import numpy as np
import pickle
import streamlit as st
import joblib
from PIL import Image
from datetime import datetime
encoder_path = "fencod_data.pkl" 
with open(encoder_path, 'rb') as f:
    encoder = pickle.load(f)
model = joblib.load('dt_joblib.pkl')


st.title("Machine Learning Prediction App")
st.header("Enter the details for prediction:")

passenger_count = st.number_input('Passenger Count', min_value=1, max_value=6, step=1)
distance_km=st.number_input('Trip Distance (km)', min_value=0.0, step=0.1)
Duration=st.number_input('Duration', min_value=1, max_value=50, step=1)
RatecodeID= st.selectbox('RateCode', ['RatecodeID_1','RatecodeID_2'])
payment_type=st.selectbox('payment_type', ['payment_type_1','payment_type_2'])
AM_PM=st.selectbox('AM_PM', ['AM','PM'])
weekday = st.selectbox('Day of the Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
input_data = pd.DataFrame({
    'passenger_count': [passenger_count],
    'distance_km': [distance_km],
    'Duration': [Duration],
    'RatecodeID': [RatecodeID],
    'payment_type': [payment_type],
    'AM_PM': [AM_PM],
    'weekday': [weekday],
})
categorical_cols=['RatecodeID','payment_type','AM_PM','weekday']
continuous_cols=['passenger_count','distance_km','Duration']
encoded_user_array = encoder.transform(input_data[categorical_cols])
encoded_user_df = pd.DataFrame(encoded_user_array,columns=['RatecodeID_1','RatecodeID_2','payment_type_1','payment_type_2','AM','PM','weekday_1','weekday_3'])
final_user_df = pd.concat([input_data[continuous_cols], encoded_user_df], axis=1)

st.write("Input Data:", input_data)
if st.button('Predict Trip Price'):
    prediction = model.predict(final_user_df)
    st.write(f"The predicted amount is {prediction}.")



