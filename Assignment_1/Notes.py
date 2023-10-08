#1.1.2.a What is the 60-day simple return on Oct 18, 2022?
target_date = pd.Timestamp('2022-10-18')
date_60_days_before = target_date - pd.Timedelta(days=60)
closing_price_on_target_date = df.loc[target_date, 'Close']
closing_price_60_days_before = df.loc[date_60_days_before, 'Close']
simple_return_60 = (closing_price_on_target_date / closing_price_60_days_before) - 1
print("This is the simple return after 60 days")
print(simple_return_60)