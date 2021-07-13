import streamlit as st
import pandas as pd


@st.cache(suppress_st_warning=True)
def file(file):
    df = pd.read_csv(file)
    Community= df['Community League'].drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League:', Community)
    Program= df["Program"].loc[df["Community League"]== ComChoice]
    st.write(Program)

def check():
    #title
    st.title(""" EFCL CLOG Database """)

    #Sidebar
    st.sidebar.subheader("Visualization Settings")

    #File upload
    file= st.sidebar.file_uploader(label= "Upload your csv or excel file.", type= ['csv', 'xlsx'])

    #checking which file is uploaded 

   

 
   
    df = pd.read_csv(file)
    Community= df['Community League'].drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League:', Community)
    Program= df["Program"].loc[df["Community League"]== ComChoice]
    st.write(Program)

if __name__=="__main__":
  
    check()
   
