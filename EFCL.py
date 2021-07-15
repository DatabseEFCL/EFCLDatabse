from packaging.version import LegacyCmpKey
import streamlit as st
import pandas as pd



@st.cache(allow_output_mutation=True)
def loadData(file_uploaded):
    df = pd.read_csv(file_uploaded, encoding='unicode_escape')
    st.dataframe(df,3000,500)
    return df 

    



#title
st.title(""" EFCL CLOG Database """)
st.text("Please upload your csv file, then select topic you want to search by.")
#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file_uploaded= st.sidebar.file_uploader(label= "Upload your csv file.", type= ['csv'])
League= st.checkbox("Search by Community League",key='1')
Prog= st.checkbox("Search by Program",key='2')

st.write(League)
st.write(Prog)

while file_uploaded is not None:
    df= loadData(file_uploaded)
    while file_uploaded:
        if League:
            Community= df['Community League'].drop_duplicates()
            ComChoice= st.sidebar.selectbox('Select your Community League:', Community, )
            Program= df["Program"].loc[df["Community League"] & df["Delivery"].loc[df["Community League"]== ComChoice]]
            st.table(Program)
        if Prog:
            Community= df['Program']
            ComChoice= st.sidebar.selectbox('Select your Community League:', Community, key = '1')
            Delivery= df["Delivery"].loc[df["Community League"]== ComChoice]
            st.table(Delivery)

