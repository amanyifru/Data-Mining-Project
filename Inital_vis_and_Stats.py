import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv('/path/to/your/Modified_PSDH_Power_Supply_Evaluation.csv')

# Compute summary statistics for the numerical columns
summary_stats = data.describe()
print(summary_stats)

# Create histograms for 'Duration (Hours)' and 'Number of Customers Affected'
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Histogram for 'Duration (Hours)'
sns.histplot(data['Duration (Hours)'], bins=30, kde=True, ax=ax[0])
ax[0].set_title('Distribution of Outage Duration (Hours)')

# Histogram for 'Number of Customers Affected'
sns.histplot(data['Number of Customers Affected'], bins=30, kde=True, ax=ax[1])
ax[1].set_title('Distribution of Number of Customers Affected')

plt.tight_layout()
plt.show()
