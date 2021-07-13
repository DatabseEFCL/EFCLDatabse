import streamlit as st
import pandas as pd
import numpy as np

def file():

    #title
    st.title(""" EFCL CLOG Database """)
    st.write("Please upload file to the application.")


    #Sidebar
    st.sidebar.subheader("Visualization Settings")

    #File upload
    file= st.sidebar.file_uploader(label= "Upload your csv or excel file.", type= ['csv', 'xlsx'])

   

    global df

    if file is not None:
        print(file)
        try: 
            df = pd.read_csv(file)
            st.markdown('Your csv file has been uploaded !')
        except Exception as e: 
            print(e)
            df= pd.read_excel(file)
            st.markdown('Your excel file has been uploaded !')

    
        


if __name__=="__main__":
    file()
