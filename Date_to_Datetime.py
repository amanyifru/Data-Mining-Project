import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Modified_PSDH_Power_Supply_Evaluation_with_DateTime.csv')

data['Date'] = pd.to_datetime(data['Date'])

data.set_index('Date', inplace=True)
data['Count'] = 1 
data.resample('M').sum()['Count'].plot(kind='line', figsize=(10, 5))
plt.title('Frequency of Power Outages Over Time')
plt.ylabel('Number of Outages')
plt.xlabel('Date')
plt.show()
