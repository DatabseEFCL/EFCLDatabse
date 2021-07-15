from packaging.version import LegacyCmpKey
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
st.text("Please upload your csv file and select topic you want to search by.")
#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file_uploaded= st.sidebar.file_uploader(label= "Upload your csv file.", type= ['csv'], key ='file_uploader')
League= st.checkbox("Search by Community League",key='1')
Prog= st.checkbox("Search by Program",key='2')

st.write(League)
st.write(Prog)

while file_uploaded is not None:
    df= loadData(file_uploaded)
'''
    Community= df['Community League'].drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League:', Community, key = '1')
    Program= df["Program"].loc[df["Community League"]== ComChoice]
    st.write(Program)

'''
    
