import pandas as pd

df = pd.read_csv('FSELX.csv')
df = pd.read_csv('IVW.csv')
df = pd.read_csv('IVE.csv')

#2.2.1 We want to know if the coefficient on the growth fund price movements is statistically 
#significant. State your hypotheses.
#My work is in the document

#2.2.2 Perform a single parameter test (t test) for the importance of growth fund price movements 
#in your model and interpret the result.
from scipy import stats

B1_t_statistic = 25.308  
df = 503
# Calculating two-tailed p-value
B1_p_value = stats.t.sf(abs(B1_t_statistic), df) * 2
print("The following is the p-value for B1")
print(B1_p_value)



B2_t_statistic = 19.763  
df = 503
# Calculating two-tailed p-value
B2_p_value = stats.t.sf(abs(B2_t_statistic), df) * 2
print("The following is the p-value for B2")
print(B2_p_value)



#2.2.3 Perform a joint test of the growth fund and value fund price movements in explaining the 
#price movements in the FSELX fund: state your hypotheses, perform the test using both F statistic 
#and Chi-squared distribution, and interpret the result.

from scipy.stats import f

F_stat = 877.2
df1 = 2  
df2 = 503

p_value = f.sf(F_stat, df1, df2)

print("P-value:", p_value)
