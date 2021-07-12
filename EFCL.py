import streamlit as st
import pandas as pd

#title
st.title(""" EFCL CLOG Database """)

#Sidebar
st.sidebar.subheader("Settings")

#File upload
st.sidebar.file_uploader(label= "Upload your csv or excel file.")
