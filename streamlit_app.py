!pip install matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hello World")

st.write("*Data Science Course 2024*")

df = pd.read_csv("data/Bastar Craton.csv")

cat_names = df.columns.tolist()[27:]

col1, col2 =st.columns(2)

with col1:
    el1 = st.selectbox("x-axis", cat_names)
    el2 = st.selectbox("y-axis", cat_names)

with col2:
    fig=plt.figure
    plt.scatter([1,2,3], [4,5,6])
    st.pyplot(fig)

st.dataframe(df)