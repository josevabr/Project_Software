# Project_Software
 Repository for software development project
 
 Introduction
 Creating and managing python virtual environments, developing a web application, and deploying it to a cloud service that will make it accessible to the public.
 
 Step 1: Prerequisites 
 
Installed the following packages: pandas, streamlit, plotly-express. 
Created an account on render.com, linked it to my GitHub account
Installed VS Code, loaded the project directory and set the Python interpreter to the one used by the virtual environment
Used car advertisement dataset (vehicles_us.csv) 

Step 2: Exploratory Data Analysis

Created an EDA.ipynb Jupyter notebook in VS Code
Performed some basic exploratory analysis of the dataset in the notebook (searched for duplicates/missing values, replaced values, searched for counts in columns to be used for graphs)
Created a couple of histograms and scatterplots using plotly-express library
 -Compared distribution of price in cars, distribution of models in cars, distribution of price by model of cars, and distribution of price by model year in cars.

Step 3: Develop the web application dashboard

Created an app.py file in the root of the project’s directory
Imported streamlit, pandas and plotly_express
Read the dataset’s CSV file into a DataFrame
Copied from the Jupyter notebook:
-at least one st.header with text
-at least one plotly-express histogram using st.write
-at least one plotly-express scatter plot using st.write
-at least one checkbox using st.checkbox that changes the behavior of any of the above components

Step 4: Deploy the final version of the application to Render

Added a streamlit configuration file to your git repository at .streamlit/config.toml with the following content:
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
Uploaded web application to Render


URL for app on Render:

https://project-software.onrender.com
