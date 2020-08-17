import scipy.stats
import streamlit as st

import math
n1=230
n2=540
x1=100
x2=200

#Sample proportion
p1_hat=x1/n1
print("p1 hat : ",p1_hat)

p2_hat=x2/n2
print("p2 hat : ",p2_hat)




confidence_level=95
significance_level=1-(confidence_level)/100

z_critical_value=scipy.stats.norm.ppf(1-significance_level/2)

lhs=p1_hat-p2_hat
rhs=z_critical_value*math.sqrt((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2))

confidence_interval_lhs,confidence_interval_rhs=(lhs-rhs,lhs+rhs)
print(confidence_interval_lhs," < p < ",confidence_interval_rhs)