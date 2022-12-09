import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta

def app():
    st.title('Model 4 - ARIMA')
    
    #start = '2004-08-18'
    #end = '2022-01-20'
    start = st.date_input('Start' , value=pd.to_datetime('2004-08-18'))
    end = st.date_input('End' , value=pd.to_datetime('today'))
    
    st.title('Predicción de tendencia de acciones')

    user_input = st.text_input('Introducir cotización bursátil' , 'NTDOY')

    df = datas.DataReader(user_input, 'yahoo', start, end)

    st.subheader('Tabla de datos') 
    st.write(df)
    st.subheader('Datos del 2004 al 2022') 
    st.write(df.describe())

