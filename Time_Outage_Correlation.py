import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Final_PSDH_Power_Supply_Evaluation.csv')

data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month

data['Kiremt_Season'] = data['Month'].apply(lambda x: 1 if x in [6, 7, 8, 9] else 0)

monthly_outages = data.groupby('Month').agg(Total_Customers_Affected=('Number of Customers Affected', 'sum')).reset_index()

monthly_data = monthly_outages.merge(data[['Month', 'Kiremt_Season']].drop_duplicates(), on='Month')

correlation_matrix = monthly_data[['Total_Customers_Affected', 'Kiremt_Season']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix for Monthly Outages vs. Kiremt Season')
plt.show()
