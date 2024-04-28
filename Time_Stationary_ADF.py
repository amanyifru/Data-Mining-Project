from statsmodels.tsa.stattools import adfuller
import pandas as pd

data = pd.read_csv('Final_PSDH_Power_Supply_Evaluation.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

monthly_customers_affected = data['Number of Customers Affected'].resample('M').sum()

adf_result = adfuller(monthly_customers_affected)

print('ADF Statistic: %f' % adf_result[0])
print('p-value: %f' % adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print('\t%s: %.3f' % (key, value))

if adf_result[1] < 0.05:
    print("The time series is stationary.")
else:
    print("The time series is not stationary.")
