#1.1.2
new_df = pd.read_csv('AAPL.csv', parse_dates=['Date'], index_col='Date')
new_df = df.sort_index()
monthly_prices = new_df['Adj Close'].resample('M').last()
print(monthly_returns)


monthly_returns = np.log((df_last_day + 0.07666666666) / df_first_day)