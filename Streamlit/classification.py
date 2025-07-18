import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target  
    return df, iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['target'])

st.title("Iris Flower Classification")
st.write("This app classifies Iris flowers based on their features.")

st.sidebar.title("User Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

user_input = [[sepal_length, sepal_width, petal_length, petal_width]]

# Make prediction
prediction = model.predict(user_input)
# prediction_proba = model.predict_proba(user_input)
predicted_class = target_names[prediction][0]

st.write("Prediction:")
st.write(f"The Predicted species is: {predicted_class}")
# st.write(f"Prediction Probability of {predicted_class} is {prediction_proba}:")
