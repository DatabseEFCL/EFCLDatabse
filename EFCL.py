import streamlit as st
import pandas as pd
import googlemaps




#title and subheader
st.title("EFCL CLOG Database Application")
st.write("Please upload your csv file, then select topic you want to search by.")

#Sidebar
st.sidebar.subheader("Visualization Settings")
file_uploaded= st.sidebar.file_uploader(label= "Upload your 'CLOG' csv file.", type= ['csv'], key='a') #upload clog csv file

#chaching/saving CLOG data
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def loadData(file_uploaded):

    st.write("Your file has been uploaded !")
    st.write("CAUTION: DO NOT select the option 'nan', it will cause a bug and you will have to refreash the page and insert the csv file again.")
    gmaps = googlemaps.Client(key='AIzaSyAG23fb_Mhco1Xvlft4uhCqbU8h-d5-7w4')
    df = pd.read_csv(file_uploaded, encoding='unicode_escape')
    
    return df,gmaps

       

def database(file_uploaded):
        

        #function to view the databse
        if file_uploaded:
           
            df= loadData(file_uploaded)
            st.write("Your file has been uploaded !")
            st.write("CAUTION: DO NOT select the option 'nan', it will cause a bug and you will have to refreash the page and insert the csv file again.")
            Qst= st.selectbox("Choose the field you want to search by:",list(df.head()),key = "1")
            
            if file_uploaded is not None:
                
                        
                if Qst == "Community League": #outout if the selected field is community league
                        Com=df['Community League'].sort_values().drop_duplicates()
                        Com_choice= st.selectbox("Select the Community League:",list(Com),key = "2")
                        Program= df["Program"].loc[df['Community League']== Com_choice] 
                        Delivery = df["Delivery"].loc[df['Community League']== Com_choice]
                        st.table(pd.concat([Program, Delivery], axis=1))
                        
                        
                if Qst == "Program":#outout if the selected field is Program
                        Program = df["Program"].drop_duplicates().sort_values()
                        Program_ch= st.selectbox("Select the Program:",list(Program),key = '3')
                        Community= df["Community League"].loc[df['Program']== Program_ch]
                        Delivery = df["Delivery"].loc[df['Program']== Program_ch]
                        st.table(pd.concat([Community, Delivery], axis=1))
                
                if Qst == "Delivery":#outout if the selected field is Delivery 
                        Delivery= df["Delivery"].drop_duplicates().sort_values()
                        D_ch= st.selectbox("Select the method of program delivery:",list(Delivery), key = '4')
                        P_lower= df["Program"].astype(str).str.lower()
                        Program= P_lower.loc[df['Delivery']== D_ch] 
                        Community= df["Community League"].loc[df['Delivery']== D_ch]
                        st.table(pd.concat([Program, Community], axis=1))

                if Qst == "Address":#outout if the selected field is Delivery 
                        gmaps = googlemaps.Client(key='AIzaSyAG23fb_Mhco1Xvlft4uhCqbU8h-d5-7w4')
                        st.write("Address file has been uploaded !")
                        League= st.selectbox("Select Community League :", list(df["Community League"]),key='z')
                        StreetAd= df["Street Address"].loc[df['Community League']== League]
                        #st.write(StreetAd)
                        user_input= st.text_input("Please input user address.","",key="g")
                        my_dist = gmaps.distance_matrix(user_input,StreetAd)['rows'][0]['elements'][0]["distance"]["text"] # api calling distance
                        my_dur = gmaps.distance_matrix(user_input, StreetAd)['rows'][0]['elements'][0]["duration"]["text"]# api calling duration\
                        st.write("The distance is ",my_dist) #destinaton output 
                        st.write("The duration is ",my_dur) #duration output
                
                else:
                        st.write("There is no file uploaded.")

if __name__== "__main__":
        database(file_uploaded)

        
