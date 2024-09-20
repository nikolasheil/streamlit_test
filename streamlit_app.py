import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("Hello World")

st.write("*Data Science Course 2024*")

datasets = os.listdir("data")

theOne = st.selectbox("select dataset", datasets)

df = pd.read_csv(theOne)  # DAy 3 list and ends with CSV

cat_names = df.columns.tolist()[27:]

col1, col2 = st.columns(2)

with col1:
    el1 = st.selectbox("x-axis", cat_names)
    el2 = st.selectbox("y-axis", cat_names)

with col2:
    fig=plt.figure()
    plt.scatter(df[el1]/10000, df[el2]/10000)
    st.pyplot(fig)

st.dataframe(df)