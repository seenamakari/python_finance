import pandas as pd

# Read your dataset into a DataFrame
df = pd.read_csv('WE.csv')

# Set the date column as the index
df.set_index('Date', inplace=True)

#Adding the column for simple daily returns
df['simple_daily_return'] = (df['Close'] / df['Open'] - 1)

# Answer for a
simple_return_2022_06_23 = df.loc['2022-06-23']
print(simple_return_2022_06_23)

#Answer for b
simple_return_2022_07_01 = df.loc['2022-07-01']
print(simple_return_2022_07_01)

#Answer for c
simple_return_2023_03_28 = df.loc['2023-03-28']
print(simple_return_2023_03_28)




