#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 00:19:41 2025

@author: user
"""
import pandas as pd
import datetime
import xgboost as xgb
import streamlit as st


def main():
    html_temp = """
    <div style="background-color:#0d6efd;padding:12px;border-radius:10px">
    <h1 style="color:white;text-align:center;font-family:sans-serif;">
    🚗 Car Price Prediction App
    </h1>
    <p style="color:white;text-align:center;font-size:16px;">
    Enter details below to estimate the price of your car using machine learning.
    </p>
    </div>
    """
    model = xgb.XGBRegressor()
    model.load_model('xgb_model (1).json')
    st.markdown(html_temp,unsafe_allow_html=True)

    st.write('')

    p1 = st.number_input("What is the current ex showroom price of the car (in Dollars)",2.5,25.0,step=1.0)
    p2 = st.number_input("What is distance completed by the car in kilometers",500,500000,step=100)
    s1 = st.selectbox("What is the fuel type of the car?",('Petrol','Diesel','CNG'))
    if s1 =="Petrol":
        p3=0
    elif s1 =="Diesel":
        p3=1
    elif s1 =="CNG":
        p3=2

    s2 = st.selectbox("Are you a Dealer or Individual?",('Dealer','Individual'))
    if s2 =="Dealer":
        p4=0
    elif s2 =="Individual":
        p4=1
    s3 = st.selectbox("What is the transmission type?",('Manual','Automatic'))
    if s3 =="Manual":
        p5=0
    elif s3 =="Automatic":
        p5=1
    p6 = st.slider("number of owners the car previously had",0,3)
    date_time=datetime.datetime.now()
    years = st.number_input("In which year was the car purchased",1990,date_time.year)
    p7 = date_time.year - years

    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7,
  },index=[0])

    if st.button('Predict'):
        pred = model.predict(data_new)
        st.balloons()
        st.success("Estimated Car Price {:.2f} Dollar".format(pred[0]))




if __name__ == '__main__':
    main()
