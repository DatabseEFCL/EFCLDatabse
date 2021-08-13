import streamlit as st
import pandas as pd
import googlemaps
import pip 


#title
st.title(""" EFCL CLOG Database """)
st.text("Please upload your csv file, then select topic you want to search by.")
#Sidebar
st.sidebar.subheader("Visualization Settings")
SideOption= st.sidebar.selectbox("Select the fields to use",options=("Map","Dataset")) #choose between Map or Data


def import_or_install(googlemaps):
        try:
                import googlemaps
        except ModuleNotFoundError:
                pip.main(['install',googlemaps])

#chaching/saving CLOG data
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def loadData(file_uploaded):

    st.write("Your file has been uploaded !")
    st.write("CAUTION: DO NOT select the option 'nan', it will cause a bug and you will have to refreash the page and insert the csv file again.")

    df = pd.read_csv(file_uploaded, encoding='unicode_escape')
    
    return df

#caching address 
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def map(file_uploaded2):
     
     df= pd.read_csv(file_uploaded2, encoding='unicode_escape')
     st.write("There is no file uploaded")
     st.write("Address file has been uploaded !")
     return df
       

def database():
        file_uploaded= st.sidebar.file_uploader(label= "Upload your 'CLOG' csv file.", type= ['csv'], key='a') #upload clog csv file

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
        

def Directions():
        file_uploaded2= st.sidebar.file_uploader(label= "Upload your 'League Addresses' csv file.", type= ['csv'], key='x') #upload address file
        # Requires API key
        gmaps = googlemaps.Client(key='AIzaSyAG23fb_Mhco1Xvlft4uhCqbU8h-d5-7w4')


        if file_uploaded2 is not None:
                df= map(file_uploaded2) #calls map funciton 

                if file_uploaded2 :
                        st.write("Address file has been uploaded !")
                        League= st.selectbox("Select Community League :", list(df["Community League"]),key='z')
                        MailAd= df["Mailing Address"].loc[df['Community League']== League]
                        StreetAd= df["Street Address"].loc[df['Community League']== League]

                        ratio = st.radio("Select the type of Addrress",['Street Address','Mailing Address'], key='y')

                        if ratio == "Street Address":
                                destination_input= st.write(StreetAd)
                                user_input= st.text_input("Please input user address.","",key="g")
                                my_dist = gmaps.distance_matrix(user_input,destination_input)['rows'][0]['elements'][0]["distance"]["text"] # api calling distance
                                my_dur = gmaps.distance_matrix(user_input, destination_input)['rows'][0]['elements'][0]["duration"]["text"]# api calling duration
                                st.write("The distance is ",my_dist) #destinaton output 
                                st.write("The duration is ",my_dur) #duration output

                        if ratio == "Mailing Address":
                                destination_input2= st.write(MailAd)
                                user_input2= st.text_input("Please input user address.","",key="h")
                                my_dist2 = gmaps.distance_matrix(user_input2,destination_input2)['rows'][0]['elements'][0]["distance"]["text"] # api calling distance
                                my_dur2 = gmaps.distance_matrix(user_input2, destination_input2)['rows'][0]['elements'][0]["duration"]["text"]# api calling duration
                                st.write("The distance is ",my_dist2)#destinaton output 
                                st.write("The duration is ",my_dur2) #duration output
                else:
                        st.write("There is no file uploaded")

if __name__== "__main__":
        if SideOption == "Dataset": #if sidebar option is Dataset then the clog databse function will run.

                database()

        if SideOption == "Map": #if map is selected then addresses and directions will be shown.
                Directions()
        
