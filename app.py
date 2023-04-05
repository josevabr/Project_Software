import streamlit as st
import pandas as pd
import plotly.express as px 

df = pd.read_csv('vehicles_us.csv')



st.header('Distribution of Price in Cars')
fig = px.histogram(df, x = "price", title = "Distribution of Price in Cars")
st.write(fig)

st.header('Distribution of Models in Cars')
fig = px.histogram(df, x = 'model', title = 'Distribution of Models in Cars')
st.write(fig)

st.header("Distribution of Price by Models in Cars")
fig = px.scatter(df, x = 'price', y = 'model', log_x=[0, 300000], title = 'Distribution of Price by Model of Cars')
st.write(fig)

model_options = df['model'].unique().tolist()
model = st.selectbox('Car Model', model_options, 0)
df = df[df['model']== model]

st.header("Distribution of Price by Model Years in Cars")
fig = px.scatter(df, x = 'model_year', y = 'price', log_y=[1, 1000], title = 'Distribution of Price by Model Year in Cars')
st.write(fig)

check = st.checkbox('This app works!')
st.write('State of the checkbox:', check)
