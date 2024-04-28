import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

data = pd.read_csv('Final_PSDH_Power_Supply_Evaluation.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

monthly_customers_affected = data['Number of Customers Affected'].resample('M').sum()

model = ARIMA(monthly_customers_affected, order=(1, 0, 1))  
fitted_model = model.fit()

forecast = fitted_model.get_forecast(steps=12)
mean_forecast = forecast.predicted_mean
conf_int = forecast.conf_int()

plt.figure(figsize=(10, 5))
plt.plot(monthly_customers_affected.index, monthly_customers_affected, label='Observed')
plt.plot(mean_forecast.index, mean_forecast, color='red', label='Forecast')
plt.fill_between(mean_forecast.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.3)
plt.xlabel('Date')
plt.ylabel('Number of Customers Affected')
plt.title('ARIMA Forecast of Power Outages')
plt.legend()
plt.show()
