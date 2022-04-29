from operator import ne
from turtle import title
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="CryptoAnalysis",
    page_icon="🧊",
    #layout="wide",
    #initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://github.com/ivanrepi",
        "Report a bug": "https://github.com/ivanrepi",
        "About": "# This app serves is an MVP for interactive dashboards that can be used for financial data analysis",
    },
)

st.title("Cryptocurrencies Investment Helper")
#st.subheader("Ivan Repilado - Ironhack")
#st.markdown("This application takes into account the Top Cryptocurrencies in the market")


options_list = ['Cryptocurrencies Analysis', 'Price Prediction', 'Buy & Sell']

st.sidebar.title("Market Helper")
st.sidebar.markdown("This app will help you on data analysis, price prediction and other helpful tools for the investment decisions")
select = st.sidebar.selectbox("Select an Option:", options_list, key='1')




