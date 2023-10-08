import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

df_FSELX = pd.read_csv('FSELX.csv')
df_IVW = pd.read_csv('IVW.csv')
df_IVE = pd.read_csv('IVE.csv')

FSELX = df_FSELX['Adj Close']
IVW = df_IVW['Adj Close']
IVE = df_IVE['Adj Close']

merged_df = pd.concat([FSELX, IVW, IVE], axis=1)
merged_df.columns = ['FSELX', 'IVW', 'IVE']

y = merged_df['FSELX']  # Dependent variable
x = merged_df[['IVW', 'IVE']]  # Independent variables

merged_df = pd.concat([FSELX, IVW, IVE], axis=1)
merged_df.columns = ['FSELX', 'IVW', 'IVE']

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(x, y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# with statsmodels
x = sm.add_constant(x) # adding a constant
 
model = sm.OLS(y, x).fit()
predictions = model.predict(x) 
 
print_model = model.summary()
print(print_model)



#2.1.1 Write the regression model (answer in the PDF)


#2.1.2 Run the regression, report the estimated coefficients (parameters) for intercept (using alpha 
#notation) and slopes (using beta notation), along with their corresponding standard errors.


#2.1.3 Using the reported coefficients for the intercept and the slope, write your SRF (sample 
#regression function), and plot the OLS residuals.


#2.1.4 Interpret what the value for your intercept, and the other two coefficients mean in your 
#model.



#2.1.5 2.1.5 If in a given day the growth fund price was $95 and the value fund was $100, what would be 
#the price on the FSELX fund?

