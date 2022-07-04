import streamlit as st
import macro
import macro.macro_data
import plotly.express as px

def display_inflation():
    with st.container():
        cpi = macro.macro_data.get_cpi(macro.fred)
        corecpi = macro.macro_data.get_core_cpi(macro.fred)
        st.header("Inflation")
        col1, col2 = st.columns(2)
        with col1:
            st.text("CPI for all Urban Consumers: All Items in U.S. City Average")
            fig = px.line(x=cpi.index,y=cpi,labels={'x': 'Date', 'y': 'CPI '})
            st.plotly_chart(fig, use_container_width=True)
            st.text("CPI for all Urban Consumers: All Items less Food and Energy")
            fig = px.line(x=corecpi.index,y=corecpi,labels={'x': 'Date', 'y': 'Core CPI'})
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.text("CPI for all Urban Consumers: All Items in U.S. City Average YOY%")
            cpiyoy=cpi.pct_change(12)*100
            fig = px.line(x=cpiyoy.index,y=cpiyoy,labels={'x': 'Date', 'y': 'CPI YOY%'})
            st.plotly_chart(fig, use_container_width=True)
            st.text("CPI for all Urban Consumers: All Items in U.S. City Average YOY%")
            corecpiyoy=corecpi.pct_change(12)*100
            fig = px.line(x=corecpiyoy.index,y=corecpiyoy,labels={'x': 'Date', 'y': 'Core CPI YOY%'})
            st.plotly_chart(fig, use_container_width=True)
        
        st.text("CPI Components")
        cpicomponents=macro.macro_data.get_cpi_components(macro.fred)
        
        fig = px.bar(cpicomponents, x="Components", y="Inflation",color="Components")
        st.plotly_chart(fig, use_container_width=True)

        return





