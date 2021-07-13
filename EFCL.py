import streamlit as st
import pandas as pd


#title
st.title(""" EFCL CLOG Database """)

#Sidebar
st.sidebar.subheader("Visualization Settings")

#File upload
file= st.sidebar.file_uploader(label= "Upload your csv or excel file.", type= ['csv', 'xlsx'])

        
#checking which file is uploaded 
def file_upload():
        
    global df

    if file is not None:
        print(file)
        try: 
            df = pd.read_csv(file)
        except Exception as e:
            print(e)
            df= pd.read_excel(file)
    try:
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application.")
    return df
@st.cache
def main(df):

    path = df
    return path
    df = main()

    ComL= df['Community League']. drop_duplicates()
    ComChoice= st.sidebar.selectbox('Select your Community League: ', ComL)
    Prog= df["Program"].loc[df["Community League"]== ComChoice]
    ProgChoice= st.sidebar.selectbox('Select your Program', Prog)

if __name__ == "__main__":
    main(df)
