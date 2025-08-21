# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:40:34 2024

@author: ahuja
"""
# app.py

import streamlit as st
import pickle
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

with open('sarima_model.pkl', 'rb') as f:
    sarima_model = pickle.load(f)

def predict_aqi(model, start_date, periods):
    forecast = model.get_forecast(steps=periods)
    predicted_aqi = forecast.predicted_mean
    return predicted_aqi

# Title for the Streamlit app
st.title('VAYU Air Quality Index (AQI) Prediction')
st.write("""
This tool allows you to predict AQI for a specific time period.  
Just provide the necessary inputs below.
""")
st.subheader('1. Select Start Date')
start_date = st.date_input('Select a start date for prediction')
st.subheader('2. Enter Number of Days to Forecast')
periods = st.number_input('Number of days to predict', min_value=1, max_value=365, value=7)
st.subheader('3. Select City')
city = st.selectbox(
    'Select the city for AQI prediction',
    ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad']
)
# Prediction button
if st.button('Predict AQI'):
    # Get the prediction using SARIMA
    predictions = predict_aqi(sarima_model, start_date, periods)
    
    # Display results
    st.subheader(f'Predicted AQI for {city} for the next {periods} days starting from {start_date}:')
    
    # Convert predictions to a DataFrame for better display
    pred_df = pd.DataFrame({
        'Date': pd.date_range(start=start_date, periods=periods),
        'Predicted AQI': predictions
    })

    st.write(pred_df)

# Sidebar information about AQI ranges
st.sidebar.title("AQI Information")
st.sidebar.write("""
- **0 - 50**: Good  
- **51 - 100**: Moderate  
- **101 - 150**: Unhealthy for Sensitive Groups  
- **151 - 200**: Unhealthy  
- **201 - 300**: Very Unhealthy  
- **301 and above**: Hazardous  
""")

st.sidebar.write("Learn more about AQI and how it affects health at [EPA AQI Guide](https://www.airnow.gov/aqi/aqi-basics/).")

# Footer
st.write("""
#### Note:
This prediction is based on historical AQI data and a SARIMA model. Please use the forecast responsibly.
""")

