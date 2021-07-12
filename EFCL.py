import streamlit as st
import pandas as pd



#title
st.title(""" EFCL CLOG Database """)

#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file= st.sidebar.file_uploader(label= "Upload your csv or excel file.", type= ['csv', 'xlsx'])

global df
if file is not None:
    print(file)

    try: 
        df = pd.read_csv(file)
    except Exception as e:
        print(e)
        df= pd.read_excel(file)
try:

    st.write(df)
except Exception as e:
    print(e)
    str.write("Please upload file to the application.")
