import math
import scipy.stats
import numpy as np
import scipy.special as scsp

# sample size n
n=100

# sample mean x_bar
x_bar=110

# Standard deviation sigma
sigma=40

# significance_level
significance_level=0.05

z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
# Confidence interval
c_i_minus,c_i_plus=x_bar-z_critical*((sigma)/(math.sqrt(n))),x_bar+z_critical*((sigma)/(math.sqrt(n)))
print(c_i_plus,c_i_minus)
print(f"lower bound {c_i_plus}")
print(f"upper bound {c_i_minus}")