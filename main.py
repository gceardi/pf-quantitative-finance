import pandas as pd
import numpy as np
import yfinance as yf

# descargar precios desde yahoo finance
tickers = ["IVV", "ILF", "SOXX"] #SP500, LATAM y SEMICONDUCTORES
vector_w = [0.5,0.3,0.2] # lista de pesos
vector_w = np.array(vector_w).reshape(-1,1) #vector de pesos
df_prices = yf.download(tickers, start="2024-01-01", end="2026-09-30")["Close"]

# calcular retornos diarios
df_ret = df_prices.pct_change().dropna()

# calcular matriz de varianza covarianza
df_cov = df_ret.cov()

# calcular la varianza del portafolio
w = vector_w
w_t = w.T
sigma = df_cov.values
varianza = np.dot(w_t, np.dot(sigma,w))
varianza1 = np.dot(np.dot(w_t,sigma),w)
#print(varianza)
#print(varianza1)

# calcular la desviacion estandar
desv = varianza[0][0]**(0.5)
volatilidad_anual = desv*252**(0.5)
print(f"La volatilidad anual del portafolio es : {volatilidad_anual*100 :.4}%")