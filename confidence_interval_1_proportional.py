import math

import scipy.stats
n=70
x=30
significance_level=0.05
p_cap=x/n
z=scipy.stats.norm.ppf(1-significance_level/2)
confidance_interval_left,confidance_interval_right=p_cap-z*math.sqrt(p_cap*(1-p_cap)/n),p_cap+z*math.sqrt(p_cap*(1-p_cap)/n)

print(z )

print(confidance_interval_left,confidance_interval_right)