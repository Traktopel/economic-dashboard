import streamlit as st
import macro
import macro.macro_data
import plotly.express as px

def display_gdp():
    with st.container():
        st.header("Gross Domestic Product")
        gdp = macro.macro_data.get_gdp(macro.fred)
        realgdp = macro.macro_data.get_real_gdp(macro.fred)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Nominal GDP, Billions of US Dollars")
            fig = px.line(x=gdp.index,y=gdp,labels={'x': 'Date', 'y': 'GDP '})
            st.plotly_chart(fig, use_container_width=True)
            st.text("Real GDP, Billions of Chained 2012 Dollars")
            fig = px.line(x=realgdp.index,y=realgdp,labels={'x': 'Date', 'y': 'Real GDP '})
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.text("Nominal GDP, YoY pct of change")
            gdpyoy=gdp.pct_change(4)*100 # YoY for quarterly data
            fig = px.line(x=gdpyoy.index,y=gdpyoy,labels={'x': 'Date', 'y': 'GDP YOY%'})
            st.plotly_chart(fig, use_container_width=True)
            st.text("Real GDP, YoY pct of change")
            realgdpyoy=realgdp.pct_change(4)*100 # YoY for quarterly data
            fig = px.line(x=realgdpyoy.index,y=realgdpyoy,labels={'x': 'Date', 'y': 'Real GDP YOY% '})
            st.plotly_chart(fig, use_container_width=True)
        with col3:
            st.text("Nominal GDP QoQ pct of change")
            gdpqoq=gdp.pct_change()*100 # QoQ for quarterly data
            fig = px.line(x=gdpqoq.index,y=gdpqoq,labels={'x': 'Date', 'y': 'GDP MOM%'})
            st.plotly_chart(fig, use_container_width=True)
            st.text("real GDP QoQ pct of change")
            realgdpqoq=realgdp.pct_change()*100 # QoQ for quarterly data
            fig = px.line(x=realgdpqoq.index,y=realgdpqoq,labels={'x': 'Date', 'y': 'Real GDP MOM%'})
            st.plotly_chart(fig, use_container_width=True)
        return





