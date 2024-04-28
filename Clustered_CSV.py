import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Preprocessed_PSDH_Power_Supply_Evaluation.csv')

features = data[['Scaled Duration (Hours)', 'Scaled Number of Customers Affected']].values

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
data['Cluster_Labels'] = kmeans.fit_predict(features)

clustered_data_filepath = 'Clustered_PSDH_Power_Supply_Evaluation.csv'
data.to_csv(clustered_data_filepath, index=False)

print(f"The clustered dataset has been saved to: {clustered_data_filepath}")
