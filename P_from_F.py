import scipy.stats as stats
from rpy2 import robjects




pf_val=robjects.r['pf']
x=pf_val(1.74,2,2)
print([1-y for y in x ])
# working in R
# In R, you can calculate p-value by:
# 1-pf(Fvalue, df1=v1, df2=v2)
# Hope this helps.