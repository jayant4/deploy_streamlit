from scipy import stats
import streamlit as st

st.title('P value from T test')

## Calculate the t-statistics
t =st.text_input(" Enter T value : ")
#0.408
#Degrees of freedom
df =st.text_input(" Enter Degrees of Freedom : ")

def main(t,df):
    p = 1 - stats.t.cdf(t,df)
    return str(2*p),str((2*p)/2)

# print(main(2.5,99))

if (st.button("calculate")):
  p_one_tail,p_two_tail= main(float(t),float(df))
  st.write("P One Tail value is ",p_one_tail)
  st.write("P Two Tail value is ", p_two_tail)
