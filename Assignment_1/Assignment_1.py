import pandas as pd

# Read your dataset into a DataFrame
df = pd.read_csv('WE.csv')

# Set the date column as the index
df.set_index('Date', inplace=True)



#Adding the column for simple daily returns
df['simple_daily_return'] = (df['Close'] / df['Open'] - 1)

# Retrieve data for specific dates
specific_date_data = df.loc['2022-06-23']



# Analyze or use the retrieved data
print(specific_date_data)

