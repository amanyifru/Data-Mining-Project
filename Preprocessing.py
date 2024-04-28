import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Modified_PSDH_Power_Supply_Evaluation_with_DateTime.csv')

features = data[['Duration (Hours)', 'Number of Customers Affected']]

scaler = StandardScaler()

scaled_features = scaler.fit_transform(features)

scaled_features_df = pd.DataFrame(scaled_features, columns=['Scaled Duration (Hours)', 'Scaled Number of Customers Affected'])

data[['Scaled Duration (Hours)', 'Scaled Number of Customers Affected']] = scaled_features_df

data.to_csv('Preprocessed_PSDH_Power_Supply_Evaluation.csv', index=False)

print("Preprocessed dataset saved as 'Preprocessed_PSDH_Power_Supply_Evaluation.csv'.")
