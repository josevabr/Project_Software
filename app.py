import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(
    page_title="Project Software", 
    page_icon="✅",
    layout='wide',
)
@st.cache
def get_data() -> pd.DataFrame:
    return pd.read_csv('vehicles_us.csv')

df = get_data()

st.header("Distribution of Price by Models in Cars")
fig = px.scatter(df, x = 'price', y = 'model', log_x=[0, 300000], title = 'Distribution of Price by Model of Cars')
st.write(fig)

st.header("Distribution of Price by Model Years in Cars")
fig = px.scatter(df, x = 'model_year', y = 'price', log_y=[1, 1000], title = 'Distribution of Price by Model Year in Cars')
st.write(fig)

st.title('Distribution of Price in Car Model and Car Model Years')
col1, col2, col3 = st.columns(3)
model_selection = col1.multiselect('Select Model', df['model'].unique().tolist())
df = df[df['model']==model_selection]
price_selection = col2.multiselect('Select Price', df['price'].unique().tolist())
df = df[df['price']==price_selection]
year_selection = col3.multiselect('Select Model Year', df['model_year'].unique().tolist())
df = df[df['model_year']==year_selection]

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.markdown('### Distribution of Price in Cars')
    fig = px.histogram(df, x = "price")
    st.write(fig)

with fig_col2:
    st.markdown('### Distribution of Models in Cars')
    fig = px.histogram(df, x = 'model')
    st.write(fig)

check = st.checkbox('This app works!')
st.write('State of the checkbox:', check)
