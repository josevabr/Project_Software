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
model_selection = st.multiselect('Select Model', pd.unique(df['model']))
df = df[df['model']==model_selection]
price_filter = st.selectbox('Select Price', pd.unique(df['price']))
df = df[df['price']== price_filter]
year_filter = st.selectbox('Select Model Year', pd.unique(df['model_year']))
df = df[df['model_year']== year_filter]

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
