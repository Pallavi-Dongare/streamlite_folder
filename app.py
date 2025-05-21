import requests
import pandas as pd
from client import StockApi
import plotly.graph_objects as go
import streamlit as st

#create page title

st.set_page_config(page_title="Stock market app",layout="wide")

# add title

st.title("stock market app")

# # add sub heading

st.subheader("By Pallavi Dongare")

#add box for company
company = st.text_input("company name")

#make connection between app amd api
@st.cache_resource(ttl=3600)
def fetch_data():
    return StockApi(api_key=st.secrets["API_KEY"])

stock_api = fetch_data()


#search symbol

@st.cache_data(ttl=3600)
def get_symbol(company):
    symbol = stock_api.search_symbol(company)
    return symbol


@st.cache_data(ttl=3600)
def plot_chart(symbol):
    df = stock_api.time_series_daily_data(symbol)
    fig = stock_api.plot_graph(df)
    return fig

if company:
    company_data = get_symbol(company)
    symbols = list(company_data.keys())
    options = st.selectbox("select symbols",symbols)
    selected_data = company_data.get(options)
    st.success(f"Company Name:{selected_data[0]}")
    st.success(f"Region:{selected_data[1]}")