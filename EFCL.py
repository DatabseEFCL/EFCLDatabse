import streamlit as st
import pandas as pd
from streamlit.uploaded_file_manager import UploadedFile

#title
st.title("EFCL CLOG DATABASE")

#sidebar title
st.sidebar.header("Data Visualization Settings")
#setup file upload
uploaded_file= st.sidebar.file_uploader(label="Upload your CSV or Excel file.", type = ['csv','xlsx'])

def file():

    global df
    if uploaded_file is not None:
        try:
            df= pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df= pd.read_excel(uploaded_file)
        finally:
            str.write("Please upload file to application")
    
    try:
        st.write(df)
    except Exception as e:
        str.write(e)
        st.write("The uploaded file is incorrect")
    finally:
        file()
        
def csv_file():
    
