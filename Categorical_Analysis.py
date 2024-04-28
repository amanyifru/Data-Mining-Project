import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Modified_PSDH_Power_Supply_Evaluation_with_DateTime.csv')

plt.figure(figsize=(10, 6))
sns.countplot(y='City', data=data, order = data['City'].value_counts().index)
plt.title('Number of Power Outages by City')
plt.xlabel('Number of Outages')
plt.ylabel('City')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(y='Cause', data=data, order = data['Cause'].value_counts().index)
plt.title('Common Causes of Power Outages')
plt.xlabel('Number of Outages')
plt.ylabel('Cause')
plt.show()
