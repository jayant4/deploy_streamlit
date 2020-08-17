import math

import scipy.stats

# sample size n
n=80

# sample mean x_bar
x_bar=50

# Standard deviation sigma
sigma=60

# significance_level
significance_level=0.05

# degree_of_freedom
degree_of_freedom=n-1

t_critcal=scipy.stats.t.ppf(1-significance_level/2,degree_of_freedom)

confidence_interval_minus,confidence_interval_plus=x_bar-t_critcal*sigma/math.sqrt(n),x_bar+t_critcal*sigma/math.sqrt(n)
print((confidence_interval_minus,confidence_interval_plus))

print(f"lower bound : {confidence_interval_minus}")
print(f"upper bound : {confidence_interval_plus}")