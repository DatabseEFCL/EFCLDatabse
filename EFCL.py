import streamlit as st
import pandas as pd
import os.path


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
    if os.path.isfile(file_uploaded):
        st.write("Your file has been uploaded !")
        st.write("CAUTION: DO NOT select the option 'nan', it will cause a bug and you will have to refreash the page and insert the csv file again.")
        df = pd.read_csv(file_uploaded, encoding='unicode_escape')
    else:
        st.write ("There is no file uploaded")
    
    return df


if __name__== "__main__":

        loadData(file_uploaded)

        if st.button("Access Database"):
                if file_uploaded:

                        df= loadData(file_uploaded)
                        st.write("Your file has been uploaded !")
                        st.write("CAUTION: DO NOT select the option 'nan', it will cause a bug and you will have to refreash the page and insert the csv file again.")
                        Qst= st.selectbox("Choose the field you want to search by:",list(df.head()),key = "1")
                        
                                
                        if Qst == "Community League":
                                Com=df['Community League'].sort_values().drop_duplicates()
                                Com_choice= st.selectbox("Select the Community League:",list(Com),key = "2")
                                Program= df["Program"].loc[df['Community League']== Com_choice] 
                                Delivery = df["Delivery"].loc[df['Community League']== Com_choice]
                                st.table(pd.concat([Program, Delivery], axis=1))
                                
                                
                        if Qst == "Program":
                                Program = df["Program"].drop_duplicates().sort_values()
                                Program_ch= st.selectbox("Select the Program:",list(Program),key = '3')
                                Community= df["Community League"].loc[df['Program']== Program_ch]
                                Delivery = df["Delivery"].loc[df['Program']== Program_ch]
                                st.table(pd.concat([Community, Delivery], axis=1))
                        
                        if Qst == "Delivery":
                                Delivery= df["Delivery"].drop_duplicates().sort_values()
                                col1,col2=st.beta_columns(2)
                                D_ch= st.selectbox("Select the method of program delivery:",list(Delivery), key = '4')
                                P_lower= df["Program"].astype(str).str.lower()
                                Program= P_lower.loc[df['Delivery']== D_ch] 
                                Community= df["Community League"].loc[df['Delivery']== D_ch]
                                st.table(pd.concat([Program, Community], axis=1))
        if st.button("Access Map"):

