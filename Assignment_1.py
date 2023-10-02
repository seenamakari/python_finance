import pandas as pd

# Read your dataset into a DataFrame
df = pd.read_csv('your_dataset.csv')

# Set the date column as the index
df.set_index('date_column_name', inplace=True)

# Retrieve data for specific dates
specific_date_data = df.loc['2023-10-01']
date_range_data = df.loc['2023-10-01':'2023-10-10']
specific_dates_data = df.loc[['2023-10-01', '2023-10-05', '2023-10-10']]

# Analyze or use the retrieved data
print(specific_date_data)
print(date_range_data)
print(specific_dates_data)
