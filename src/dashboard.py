import streamlit as st

from dashboard.gdp import * 
from dashboard.inflation import * 

st.set_page_config(layout="wide")

st.title("Economic Dashboard")

display_gdp()
display_inflation()