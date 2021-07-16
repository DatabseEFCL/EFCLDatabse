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
            Com=df['Community League'].sort_values().drop_duplicates()
            Com_choice= st.selectbox("Select the Community League:",list(Com),key = "2")
            Program= df["Program"].loc[df['Community League']== Com_choice] 
            Delivery = df["Delivery"].loc[df['Community League']== Com_choice]
            st.table(Program)
            st.table(Delivery)
            
    if Qst == "Program":
            Program = df["Program"].sort_values()
            Program_ch= st.selectbox("Select the Program:",list(Program),key = '3')
            Community= df["Community League"].loc[df['Program']== Program_ch]
            Delivery = df["Delivery"].loc[df['Program']== Program_ch]
            st.table(Community)
            st.table(Delivery)
    
    if Qst == "Delivery":
            Delivery= df["Delivery"].sort_values().drop_duplicates()
            col1,col2=st.beta_columns(2)
            D_ch= st.selectbox("Select the method of program delivery:",list(Delivery), key = '4')
            Program= df["Program"].loc[df['Delivery']== D_ch] 
            Community= df["Community League"].loc[df['Delivery']== D_ch]
            col1.write(Program, use_column_width=True)
            col2.write(Community, use_column_width=True)
