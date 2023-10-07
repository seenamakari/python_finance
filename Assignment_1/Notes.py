#1.1.2.a What is the 60-day simple return on Oct 18, 2022?
target_date = pd.Timestamp('2022-10-18')
date_60_days_before = target_date - pd.Timedelta(days=60)
selected_data = df.loc[date_60_days_before:target_date, ['Open', 'Close']]
simple_2022_10_18 = selected_data['Open'] - df.loc[target_date, 'Close']