import streamlit as st
import pandas as pd
import numpy as np


def file():

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
        Community= df['Community League'].drop_duplicates()
        ComChoice= st.sidebar.selectbox('Select your Community League:', Community)
        Program = df["Program"].loc[df["Community League"]== ComChoice]
        st.table(Program)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application.")




   
      
if __name__=="__main__":
    file()
