import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

outages_data = pd.read_csv('Final_PSDH_Power_Supply_Evaluation.csv')

outages_data['Date'] = pd.to_datetime(outages_data['Date'])

outages_data['Month'] = outages_data['Date'].dt.month_name()

monthly_outage_counts = outages_data.groupby('Month')['Number of Customers Affected'].count().reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

plt.figure(figsize=(12, 6))
sns.barplot(x=monthly_outage_counts.index, y=monthly_outage_counts.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Number of Outages')
plt.title('Total Number of Power Outages Per Month')
plt.tight_layout()
plt.show()
