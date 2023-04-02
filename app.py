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

st.header("Distribution of Price by Model Years in Cars")
fig = px.scatter(df, x = 'model_year', y = 'price', log_y=[1, 1000], title = 'Distribution of Price by Model Year in Cars')
st.write(fig)

check = st.checkbox('This app works!')
st.write('State of the checkbox:', check)

model_options = ['bmw x5', 'chrysler 200', 'honda pilot', 'honda accord', 'jeep cherokee', 'chevrolet tahoe', 'jeep wrangler', 'chevrolet equinox', 'honda cr-v', 'ford focus', 'chevrolet colorado', 'chevrolet cruze', 'nissan frontier crew cab sv', 'nissan versa', 'fordf250 super duty', 'subaru forester', 'ford edge', 'nissan sentra', 'ford expedition', 'acura tl', 'gmc sierra', 'gmc sierra 2500hd', 'honda odyssey', 'toyota corolla', 'toyota prius', 'toyota tundra', 'nissan frontier', 'nissan frontier', 'ford f-250 super duty', 'ford focus se', 'ford f350', 'nissan murano']
car_models = st.selectbox('Car model', options = model_options)
