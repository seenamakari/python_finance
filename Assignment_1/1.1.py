import pandas as pd
import numpy as np

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
# Setting the target date as a string
target_date = '2022-10-18'
close_price_on_target_date = df.loc[target_date, 'Close']

date_60_days_before = '2022-08-19'
close_price_60_days_before = df.loc[date_60_days_before, 'Close']

simple_60_return = (close_price_on_target_date/close_price_60_days_before) - 1
print(simple_60_return)



#1.1.2.b How about 60-day gross return on Oct 18, 2022?
gross_60_return = 1 + simple_60_return
print(gross_60_return)


#1.1.2.c What is the simple return for holding WE for the one year period (April 1, 2022 – March 31, 2023)?
last_day = '2023-03-31'
close_price_last_day = df.loc[last_day, 'Close']
print()

first_day = '2022-04-01'
close_price_first_day = df.loc[first_day, 'Close']

simple_yearly_return = (close_price_last_day/close_price_first_day) - 1
print(simple_yearly_return)




#1.1.3 Suppose you have let the returns on WE compound daily over the one-year period (April 1, 2022 – March 31, 2023). 
#What is the annual log return for WE?
log_yearly_return = np.log(31.080000) - np.log(276.799988)
#This gave me an impossible answer (-238%), so I had to calculate it using a calculator instead


#1.1.4.
#a Table with daily simple returns (already included in line 11 of this file)
#b - Table with daily log returns
df['log_daily_return'] = np.log(df['Close']) - np.log(df['Open'])

#c - Table with annualized daily simple returns
df['annualized_daily_simple_returns'] = (1 + df['simple_daily_return'])**251

#d - Table with annualized daily log returns 
df['annualized_daily_log_returns'] = (1 + df['log_daily_return'])**251

df.to_csv('1.1.4.csv')



























