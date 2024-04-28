import pandas as pd

data = pd.read_csv('Final_PSDH_Power_Supply_Evaluation.csv')

data['Quick_Response'] = (data['Comments'] == 'QR').astype(int)

print(data[['Comments', 'Quick_Response']].head())

data.to_csv('Modified_PSDH_Power_Supply_Evaluation.csv', index=False)
