import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

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

st.write("The largest number is ", greatest1)
