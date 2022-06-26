import streamlit as st
import macro
import macro.macro_data
import plotly.express as px

st.title("Economic Dashboard")
with st.container():

    gdp = macro.macro_data.get_gdp(macro.fred)
    gdp = gdp[(gdp.index > '2015-01-01')]
    fig = px.line(x=gdp.index,y=gdp,labels={'x': 'Date', 'y': 'GDP'})
    st.plotly_chart(fig, use_container_width=True)

loans=macro.macro_data.get_loans_by_type(macro.fred)

fig=px.area(loans,x='Date',y='value',color='variable')
st.plotly_chart(fig,use_container_width=True)


