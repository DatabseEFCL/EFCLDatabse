from altair.vegalite.v4.schema.core import CompositeMark
import streamlit as st
import pandas as pd
import numpy as np




@st.cache
def filter(file):
    path = r'file'
    return pd.read_csv(path)
    df = filter(file)

    Com = df['Community League'].drop_duplicates()
    Com_choice = st.sidebar.selectbox('Select your Community League:', Com)
    Program = df["Program"].loc[df["Community League"] == Com_choice]
    Prog_choice = st.sidebar.selectbox('Select your Program:', Program)
    Delivery = df["Delivery"].loc[df["Program"] == Prog_choice]
    while Program == True:
        st.table(Program) 
    while Delivery == True:
        st.table(Delivery)       

    

#def filtering(df):
        

if __name__=="__main__":

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
                
    else: 
        filter(file)

