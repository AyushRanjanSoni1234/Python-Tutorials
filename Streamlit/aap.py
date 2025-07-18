import streamlit as st
import pandas as pd
import numpy as np

# Title of the web application
st.title("Welcome to the Streamlit web application")

# Write a Input for application
st.write('This is a simple web application to demonstrate the use of Streamlit for data analysis and visualization.')

# Create a sample DataFrame
data = {
    'A': np.random.randint(1, 100, 10),
    'B': np.random.randint(1, 100, 10),
    'C': np.random.randint(1, 100, 10)
}
df = pd.DataFrame(data)
st.write("Sample DataFrame:")
st.dataframe(df)

# Create a line chart
st.write("Line Chart:")
st.line_chart(pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
), color=["#FF0000", "#0000FF","#00FF00"])

