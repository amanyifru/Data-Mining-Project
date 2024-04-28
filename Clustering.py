import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

data = pd.read_csv('Preprocessed_PSDH_Power_Supply_Evaluation.csv')

optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, random_state=42)
features = data[['Scaled Duration (Hours)', 'Scaled Number of Customers Affected']].values
cluster_labels = kmeans.fit_predict(features)

data['Cluster_Labels'] = cluster_labels

clustered_data_filepath = 'Clustered_PSDH_Power_Supply_Evaluation.csv'
data.to_csv(clustered_data_filepath, index=False)
print(f"Clustering complete. Data saved to '{clustered_data_filepath}'.")

plt.figure(figsize=(12, 8))
palette = sns.color_palette("bright", optimal_clusters)
sns.scatterplot(x=features[:, 0], y=features[:, 1], hue=cluster_labels, palette=palette, alpha=0.6, s=100, edgecolor='w')

centers = kmeans.cluster_centers_
sns.scatterplot(x=centers[:, 0], y=centers[:, 1], s=300, color='black', marker='o', label='Centroids')

plt.title('K-Means Clustering of Power Outages')
plt.xlabel('Scaled Duration (Hours)')
plt.ylabel('Scaled Number of Customers Affected')
plt.legend(loc='upper right', title='Cluster')
plt.show()
