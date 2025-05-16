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

@st.cache_resource(ttl=3600)
def fetch_data():
    return StockApi()


#create function for getting symbol
