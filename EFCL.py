
import streamlit as st
import pandas as pd

#title
st.title(""" EFCL CLOG Database """)
st.text("Please upload your csv file, then select topic you want to search by.")
#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file_uploaded= st.sidebar.file_uploader(label= "Upload your csv file.", type= ['csv'])


@st.cache(allow_output_mutation=True)
def loadData(file_uploaded):
    st.write("Your file has been uploaded !")
    df = pd.read_csv(file_uploaded, encoding='unicode_escape')
    st.dataframe(df,3000,500)
    return df

if file_uploaded:
     temp= loadData(file_uploaded)
     Qst= st.selectbox("Choose the field you want to search by",list(temp.head()))
     select_cols= st.selectbox('Choose Community League')

     if select_cols:
         st.write(select_cols)
'''
while file_uploaded is not None:
    df= loadData(file_uploaded)
   
    Community= df['Community League'].drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League:', Community, )
    Program= df["Program"].loc[df["Community League"] & df["Delivery"].loc[df["Community League"]== ComChoice]]
    st.table(Program)
'''
