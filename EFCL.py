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

    st.write("Your file has been uploaded !")
    df = pd.read_csv(file_uploaded, encoding='unicode_escape')
    
    return df



if file_uploaded:
    df= loadData(file_uploaded)

    Qst= st.selectbox("Choose the field you want to search by:",list(df.head()),key = "1")
    
        
    if Qst == "Community League":
            Com=df['Community League'].drop_duplicates()
            Com_choice= st.selectbox("Select the Community League:",list(Com),key = "2")
            Program= df["Program"].loc[df['Community League']== Com_choice] 
            Delivery = df["Delivery"].loc[df['Community League']== Com_choice]
            st.table(Program)
            st.table(Delivery)
            
    if Qst == " Program":
            Program = df["Program"]
            Prgoram_ch= st.selectboc("Select the Program:",list(Program),key = '3')
            Community= df["Community League"].loc[df['Program']== Program_ch]
            Delivery = df["Delivery"].loc[df['Program']== Program_ch]
            Result == Community 
            st.table(Result)
    
