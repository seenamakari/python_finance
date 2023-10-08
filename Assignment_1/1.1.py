import pandas as pd

# Changed dataset into a DataFrame
df = pd.read_csv('WE.csv')

# Set the date column as the index
df.set_index('Date', inplace=True)

#Adding the column for simple daily returns
df['simple_daily_return'] = (df['Close'] / df['Open']) - 1

#Adding the column for gross daily returns
df['gross_daily_return'] = 1 + df['simple_daily_return']

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

#1.1.2.a What is the 60-day simple return on Oct 18, 2022?
target_date = pd.Timestamp('2022-10-18')
date_60_days_before = target_date - pd.Timedelta(days=60)



#1.1.2.b How about 60-day gross return on Oct 18, 2022?




#1.1.2.c What is the simple return for holding WE for the one year period (April 1, 2022 – March 31, 2023)?



#1.1.3 Suppose you have let the returns on WE compound daily over the one-year period (April 1, 2022 – March 31, 2023). 
#What is the annual log return for WE?




#1.1.4.a - Table with daily simple returns
print(df)



#1.1.4.b - Table with daily log returns




#1.1.4.c - Table with annualized daily simple returns




#1.1.4.d - Table with annualized daily log returns 

















