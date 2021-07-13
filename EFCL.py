import streamlit as st
import pandas as pd

def file(file):
    df = pd.read_csv(file)
    Community= df['Community League'].drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League:', Community)
    Program= df["Program"].loc[df["Community League"]== ComChoice]
    st.write(Program)

@st.cache(suppress_st_warning=True)
def check():
    #title
    st.title(""" EFCL CLOG Database """)

    #Sidebar
    st.sidebar.subheader("Visualization Settings")

    #File upload
    file= st.sidebar.file_uploader(label= "Upload your csv or excel file.", type= ['csv', 'xlsx'])

    #checking which file is uploaded 
    global df

    if file is not None:
        print(file)
        try: 
            df = pd.read_csv(file)
            
        except Exception as e:
            print(e)
            df= pd.read_excel(file)


    Community= df['Community League'].drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League:', Community)
    Program= df["Program"].loc[df["Community League"]== ComChoice]
    st.write(Program)

if __name__=="__main__":
  
    check()
   
