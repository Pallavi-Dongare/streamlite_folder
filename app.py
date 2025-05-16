import streamlit as st
from client import StockApi

#create page title

st.set_page_config("Stock market app")

# add title

st.title("stock market app")

# add sub heading

st.subheader("By Pallavi Dongare")

# company = st.text_input("company name")

# @st.cache_resource(ttl=3600)
# def fetch_data():
#     return StockApi()


#create function for getting symbol
