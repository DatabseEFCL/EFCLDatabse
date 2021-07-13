
import streamlit as st
import pandas as pd
import numpy as np





    



#title
st.title(""" EFCL CLOG Database """)
st.text("Please upload file to the application.")


#Sidebar
st.sidebar.subheader("Visualization Settings")

#file upload
file= st.sidebar.file_uploader(label= "Upload your csv file.", type= ['csv'])

global df 

if file is not None:
        try: 
            df = pd.read_csv(file)
            st.markdown('Your csv file has been uploaded !')

        except Exception as e: 
            print(e)
st.write("hello")

