import streamlit as st
import pandas as pd


#title
st.title(""" EFCL CLOG Database """)

#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file= st.sidebar.file_uploader(label= "Upload your csv or excel file.", type= ['csv', 'xlsx'])

def upload_file():
        
    #checking which file is uploaded 
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
        st.write("Please upload file to the application.")

    return file 

@st.cache
def filter_data(df):
    ComL= df['Community League']. drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League', ComL)
    Prog= df["Program"].loc[df["Community League']= ComChoice]
    Progchoice= st.sidebar.selectbox('Select your Program',Prog)
