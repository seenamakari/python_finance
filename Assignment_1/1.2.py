import pandas as pd

# Changed dataset into a DataFrame
df = pd.read_csv('AAPL.csv')

# Set the date column as the index
df.set_index('Date', inplace=True)

#Adding the column for simple daily returns
df['simple_daily_return'] = (df['Close'] / df['Open'] - 1)

#Adding the column for gross daily returns
df['gross_daily_return'] = 1 + df['simple_daily_return']

#1.2.1 Simple returns (data: daily frequency)
#a. What is the simple return on May 06, 2022?


#b. What is the simple return on Aug 05, 2022?



#c. What about Jan 03, 2023?



#d. What is the gross return on May 06, 2022?



#e. What is the gross return on Aug 05, 2022?



#1.2.2 Log returns (data: monthly frequency)
#a. Suppose you have let the returns on AAPL compound monthly over the one-year period (April 
#1, 2022 – March 31, 2023). What is the annual log return for AAPL?



#1.2.3 Provide a table that includes the following (data: monthly frequency):


#a. Monthly simple returns


#b. Monthly log returns


#c. Bonus: annualized monthly simple returns (12 months)


#d. Bonus: annualized monthly log returns (12 months)

