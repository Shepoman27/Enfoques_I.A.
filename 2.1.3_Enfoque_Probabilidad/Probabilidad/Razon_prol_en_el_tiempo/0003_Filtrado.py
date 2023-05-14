import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Cargar datos de ejemplo (serie de tiempo mensual de ventas)
data = pd.read_csv('ventas.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

# Visualizar la serie de tiempo
data.plot()
plt.show()

# Ajustar un modelo ARIMA para filtrado, predicción y suavizado
model_arima = ARIMA(data, order=(2,1,1))
model_arima_fit = model_arima.fit()
filtered = model_arima_fit.fittedvalues
forecast = model_arima_fit.forecast(steps=12)
smoothed = model_arima_fit.predict(start=1, end=len(data))

# Ajustar un modelo SARIMA para predicción y explicación
model_sarima = SARIMAX(data, order=(2,1,1), seasonal_order=(1,1,1,12))
model_sarima_fit = model_sarima.fit()
predicted = model_sarima_fit.predict(start=len(data), end=len(data)+11)
residuals = model_sarima_fit.resid

# Visualizar resultados
plt.figure(figsize=(12,8))
plt.subplot(221)
plt.plot(data, label='Datos originales')
plt.plot(filtered, label='Filtrado')
plt.plot(smoothed, label='Suavizado')
plt.legend(loc='best')
plt.title('Filtrado y suavizado con ARIMA')

plt.subplot(222)
plt.plot(data, label='Datos originales')
plt.plot(forecast, label='Predicción')
plt.legend(loc='best')
plt.title('Predicción con ARIMA')

plt.subplot(223)
plt.plot(data, label='Datos originales')
plt.plot(predicted, label='Predicción')
plt.legend(loc='best')
plt.title('Predicción con SARIMA')

plt.subplot(224)
plt.plot(residuals)
plt.title('Residuales de SARIMA')
plt.show()
