import pandas as pd
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

data = pd.read_csv('Preprocessed_PSDH_Power_Supply_Evaluation.csv')

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, random_state=42)
features = data[['Scaled Duration (Hours)', 'Scaled Number of Customers Affected']].values
kmeans.fit(features)

data['Cluster_Labels'] = kmeans.labels_

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(features[:, 0], features[:, 1], zs=range(len(features)), c=data['Cluster_Labels'], s=50, cmap='viridis', depthshade=False)

centers = kmeans.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], zs=range(len(centers)), c='red', s=100, marker='x', label='Centroids')

ax.set_xlabel('Scaled Duration (Hours)')
ax.set_ylabel('Scaled Number of Customers Affected')
ax.set_zlabel('Index')
ax.set_title('3D visualization of K-Means Clustering')

plt.legend()
plt.show()
