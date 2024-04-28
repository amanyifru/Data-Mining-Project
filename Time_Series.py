import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

data = pd.read_csv('Final_PSDH_Power_Supply_Evaluation.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

time_series = data['Number of Customers Affected'].resample('M').sum()

decomposition = seasonal_decompose(time_series, model='additive')

plt.figure(figsize=(14, 7))
plt.subplot(411)
plt.plot(time_series, label='Original', color='blue')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(decomposition.trend, label='Trend', color='blue')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonality', color='blue')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(decomposition.resid, label='Residuals', color='blue')
plt.legend(loc='best')

plt.tight_layout()

plt.show()
