import streamlit as st
import pandas as pd



@st.cache(allow_output_mutation=True)
def loadData(file_uploaded):
    df = pd.read_csv(file_uploaded, encoding='utf-8', nrows=1552)
    df.columns = ['Community League', 'Program', 'Delivery']
    st.dataframe(df,3000,500)
    return df 

    



#title
st.title(""" EFCL CLOG Database """)

#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file_uploaded= st.sidebar.file_uploader(label= "Upload your csv file.", type= ['csv'], key ='file_uploader')

while file_uploaded is not None:
    df= loadData(file_uploaded)

    Community= df['Community League'].drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League:', Community, key = "Community")
    Program= df["Program"].loc[df["Community League"]== ComChoice]
    st.write(Program)


    
