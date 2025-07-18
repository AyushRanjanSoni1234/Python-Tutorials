import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit Widgets Example')

name = st.text_input("Enter Your Name:")
if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please enter your name.")    

age = st.slider("Select Your Age:", 0, 100, 25)
st.write(f"Your age is {age}.")

options = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
choice = st.selectbox("Select Your Favorite Language:", options)
st.write(f"You selected {choice}.")

data = [{
    'Name': 'Alice',
    'Age': 25,
    'Language': 'Python'
}, {
    'Name': 'Bob',
    'Age': 30,
    'Language': 'Java'
}, {
    'Name': 'Charlie',
    'Age': 35,
    'Language': 'C++'
}]
df = pd.DataFrame(data) 
df.to_csv('sample_data.csv', index=False)
st.write("Sample DataFrame:")
st.write(df)

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.write(df)
else:
    st.write("No file uploaded.")
