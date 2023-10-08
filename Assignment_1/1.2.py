import pandas as pd

# Changed dataset into a DataFrame
df = pd.read_csv('AAPL.csv')

# Set the date column as the index
df.set_index('Date', inplace=True)

#Adding the column for simple daily returns
df['simple_daily_return'] = (df['Close'] / df['Open']) - 1

#Adding the column for gross daily returns
df['gross_daily_return'] = 1 + df['simple_daily_return']

# 1.1.1.a What is the simple return on May 06, 2022?
data_2022_05_06 = df.loc['2022-05-06']
print(data_2022_05_06)

#1.1.1.b What the simple return on Aug 05, 2022?
data_2022_08_05 = df.loc['2022-08-05']
print(data_2022_08_05)

#1.1.1.c What about Jan 03, 2023??
data_2023_01_03 = df.loc['2023-01-03']
print(data_2023_01_03)

#1.1.1.d What is the gross return on May 06, 2022?
data_2022_05_06 = df.loc['2022-05-06']
print(data_2022_05_06)

#1.1.1.e What is the gross return on Aug 05, 2022?
data_2022_08_05 = df.loc['2022-08-05']
print(data_2022_08_05)



#1.2.2 Log returns (data: monthly frequency)
#a. Suppose you have let the returns on AAPL compound monthly over the one-year period (April 
#1, 2022 – March 31, 2023). What is the annual log return for AAPL?
new_df = pd.read_csv('AAPL.csv', parse_dates=['Date'], index_col='Date')
new_df = df.sort_index()
monthly_prices = new_df['Adj Close'].resample('M').last()
print(monthly_returns)

#1.2.3 Provide a table that includes the following (data: monthly frequency):


#a. Monthly simple returns


#b. Monthly log returns




