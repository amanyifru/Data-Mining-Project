import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Modified_PSDH_Power_Supply_Evaluation_with_DateTime.csv')

data['Date'] = pd.to_datetime(data['Date'])

correlation_matrix = data[['Duration (Hours)', 'Number of Customers Affected', 'Quick_Response']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Correlation Matrix of Variables')
plt.show()
