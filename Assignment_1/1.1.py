import pandas as pd

# Change dataset into a DataFrame
df = pd.read_csv('WE.csv')

# Set the date column as the index
df.set_index('Date', inplace=True)

#Adding the column for simple daily returns
df['simple_daily_return'] = (df['Close'] / df['Open'] - 1)

#Adding the column for gross daily returns
df['gross_daily_return'] = (df['Close'] / df['Open'] + 1)

# 1.1.1.a What is the simple return on Jun 23, 2022?
data_2022_06_23 = df.loc['2022-06-23']
print(data_2022_06_23)

#1.1.1.b What the simple return on Jul 01, 2022?
data_2022_07_01 = df.loc['2022-07-01']
print(data_2022_07_01)

#1.1.1.c What about Mar 28, 2023?
data_2023_03_28 = df.loc['2023-03-28']
print(data_2023_03_28)

#1.1.1.d What is the gross return on Jun 23, 2022?
data_2022_06_23 = df.loc['2022-06-23']
print(data_2022_06_23)

#1.1.1.e What is the gross return on Jul 01, 2022?
data_2022_07_01 = df.loc['2022-07-01']
print(data_2022_07_01)









