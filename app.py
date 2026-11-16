import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

# ====================================
# APP 
#=====================================
# titulo de la app
st.title("Calculadora Riesgo Mercado")

# seleccionar tickers
st.multiselect(label="tickers", options=["IVV", "ILF", "SOXX"], key = "tickers", default="SOXX")
tickers = st.session_state["tickers"]

# seleccionar pesos
st.multiselect(label="pesos", options=[0.5, 0.3, 0.2], key = "pesos")
vector_w = st.session_state["pesos"]
vector_w = np.array(vector_w).reshape(-1,1) #vector de pesos


# descargar precios desde yahoo finance
if len(tickers) > 0:
    df_prices = yf.download(tickers , start="2024-01-01", end="2026-09-30")["Close"]
    df_prices = df_prices[tickers]
    #st.dataframe(df_prices)

# calculo de matrices #
# calcular retornos diarios
df_ret = df_prices.pct_change().dropna()

# calcular matriz de varianza covarianza
df_cov = df_ret.cov()

# calcular la varianza del portafolio
w = vector_w
w_t = w.T
sigma = df_cov.values
varianza = (np.dot(w_t, np.dot(sigma,w)))[0][0]

# calcular la desviacion estandar
desv = varianza**(0.5)
volatilidad_anual = desv*252**(0.5)
st.write(f"La volatilidad anual del portafolio es : {volatilidad_anual*100 :.4}%")