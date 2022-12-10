import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as datas
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.tsa.seasonal import seasonal_decompose

def app():
    st.title('Model 4 - ARIMA')
    
    #start = '2004-08-18'
    #end = '2022-01-20'
    start = st.date_input('Start' , value=pd.to_datetime('2004-08-18'))
    end = st.date_input('End' , value=pd.to_datetime('today'))
    
    st.title('Predicción de tendencia de acciones')

    user_input = st.text_input('Introducir cotización bursátil' , 'NTDOY')

    df = datas.DataReader(user_input, 'yahoo', start, end)
    
    # Describiendo los datos
    st.subheader('Datos del 2004 al 2022') 
    st.write(df)
    st.subheader('Información de la Estadística descrpitiva de la data') 
    st.write(df.describe())

    #Visualizaciones 
    st.subheader('Close vs Date')
    fig = plt.figure(figsize = (15,8))
    plt.plot(df.Close)
    st.pyplot(fig)
    
    result = seasonal_decompose(data["Close"], model='multiplicative', freq = 30)
    fig = plt.figure()  
    fig = result.plot()  
    fig.set_size_inches(15, 10)
    st.pyplot(fig)
   
    # Candlestick chart
    st.subheader('Gráfico Financiero') 
    candlestick = go.Candlestick(
                            x=df.index,
                            open=df['Open'],
                            high=df['High'],
                            low=df['Low'],
                            close=df['Close']
                            )

    fig = go.Figure(data=[candlestick])

    fig.update_layout(
        width=800, height=600,
        title=user_input,
        yaxis_title='Close'
    )
    
    st.plotly_chart(fig)
      
    # Modelo ARIMA
    
    
    
    
 
