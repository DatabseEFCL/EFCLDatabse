import streamlit as st
import pandas as pd



#title
st.title(""" EFCL CLOG Database """)

#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
st.sidebar.file_uploader(label= "Upload your csv or excel file.", type= ['csv', 'xlsx'])
if file is not None:
    print("hello")
