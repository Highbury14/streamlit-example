import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")

"""
# Welcome to Streamlit! App by George J. , 21f3002389@ds.study.iitm.ac.in, Tools-for-DataScience.

Find the largest of three numbers.
"""

number1 = st.number_input("Please input the first number.")
st.write("The first number is ", number1)

number2 = st.number_input("Please input the second number.")
st.write("The second number is ", number2)

number3 = st.number_input("Please input the third number.")
st.write("The third number is ", number3)

if (number1 > number2):
    greatest1 = number1
else:
    greatest1 = number2

if (number3 > greatest1):
    greatest1 = number3

st.write("# The largest number is ", greatest1)
