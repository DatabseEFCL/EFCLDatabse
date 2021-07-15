
import streamlit as st
import pandas as pd
from collections import namedtuple

#title
st.title(""" EFCL CLOG Database """)
st.text("Please upload your csv file, then select topic you want to search by.")
#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file_uploaded= st.sidebar.file_uploader(label= "Upload your csv file.", type= ['csv'])


@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def loadData(file_uploaded):
    global df
    st.write("Your file has been uploaded !")
    df = pd.read_csv(file_uploaded, encoding='unicode_escape')
    
    return df



if file_uploaded:
    temp= loadData(file_uploaded)

    Qst= st.selectbox("Choose the field you want to search by:",list(temp.df.head()),key = "1")
    Com=temp.df['Community League'].drop_duplicates()
        
    if Qst == "Community League":
            Com_choice= st.selectbox("Select the Community League:",list(Com),key = "2")
            Com=temp.df['Community League'].drop_duplicates()
            Program= temp.df.loc[temp.df['Program']== Com_choice]
            st.table(Program)
    
