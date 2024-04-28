import pandas as pd

full_data = pd.read_csv('Clustered_PSDH_Power_Supply_Evaluation.csv')

def profile_cluster(cluster_label):
    cluster_data = full_data[full_data['Cluster_Labels'] == cluster_label]
    profile = {
        'Average Duration (Hours)': cluster_data['Duration (Hours)'].mean(),
        'Average Number of Customers Affected': cluster_data['Number of Customers Affected'].mean(),
        'Most Common City': cluster_data['City'].mode()[0],
        'Most Common Cause': cluster_data['Cause'].mode()[0],
        'Count': cluster_data.shape[0]
    }
    return profile

num_clusters = full_data['Cluster_Labels'].max() + 1  
cluster_profiles = {}

for cluster_label in range(num_clusters):
    cluster_profiles[cluster_label] = profile_cluster(cluster_label)

cluster_profiles_df = pd.DataFrame(cluster_profiles).T

print(cluster_profiles_df)

cluster_profiles_df.to_csv('Cluster_Profiles.csv', index_label='Cluster_Labels')
