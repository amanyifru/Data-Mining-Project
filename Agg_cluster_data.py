import pandas as pd

clustered_data = pd.read_csv('Clustered_PSDH_Power_Supply_Evaluation.csv')

cluster_means = clustered_data.groupby('Cluster_Labels')[['Duration (Hours)', 'Number of Customers Affected']].mean()

most_common_city = clustered_data.groupby('Cluster_Labels')['City'].apply(lambda x: x.mode()[0])
most_common_cause = clustered_data.groupby('Cluster_Labels')['Cause'].apply(lambda x: x.mode()[0])

aggregated_cluster_data = pd.concat([cluster_means, most_common_city, most_common_cause], axis=1)
aggregated_cluster_data.columns = ['Mean Duration (Hours)', 'Mean Number of Customers Affected', 'Most Common City', 'Most Common Cause']

print(aggregated_cluster_data)

aggregated_data_filepath = 'Aggregated_Cluster_Data.csv'
aggregated_cluster_data.to_csv(aggregated_data_filepath, index=False)

print("Aggregated cluster data saved to:", aggregated_data_filepath)


