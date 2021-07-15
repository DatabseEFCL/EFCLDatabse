
import streamlit as st
import pandas as pd

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
    
    Qst= st.selectbox("Choose the field you want to search by:",list(df.head()),key = "1")
    Com=df['Community League'].drop_duplicates()
    Com_choice= st.selectbox("Select the Community League:",list(Com),key = "2")
    
    
    return df


while file_uploaded:
     temp= loadData(file_uploaded)

     if Qst == "Community League":
         Com=temp['Community League'].drop_duplicates()
         Program= temp.loc[temp['Program']== Com_choice]
         st.table(Program)
      
