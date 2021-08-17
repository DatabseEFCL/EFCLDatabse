import streamlit as st
import pandas as pd
import googlemaps




#title and subheader
st.title("EFCL CLOG Database Application")
st.write("Please upload your csv file, then select topic you want to search by.")

#Sidebar
st.sidebar.subheader("Visualization Settings")


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
        global Qst 
        global df

        if file_uploaded is not None:
           
            df= loadData(file_uploaded)
            st.write("Your file has been uploaded !")
            st.write("CAUTION: DO NOT select the option 'nan', it will cause a bug and you will have to refreash the page and insert the csv file again.")
            Qst= st.selectbox("Choose the field you want to search by:",list(df.head()),key = "1")
            
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

        if Qst == "Address":#outout if the selected field is Address 
                        Directions(file_uploaded)
                
        else:
                st.write("There is no file uploaded.")
        

def Directions(file_uploaded):

        #csv file 
        df= loadData(file_uploaded)
        
        # Requires API key
        gmaps = googlemaps.Client(key='AIzaSyAG23fb_Mhco1Xvlft4uhCqbU8h-d5-7w4')

        
        Program2 = df["Program"].drop_duplicates().sort_values()


        Program= st.selectbox("Select your desired program:", list(Program2),key='z')

        StreetAd= df["Address"].loc[df['Program']== Program] #filters the addresses of programs that equal the selected program
       
        Comm= df["Community League"].loc[df['Program']== StreetAd] #finds the community leagues of the filtered addresses

        #st.write(StreetAd)
        user_input= st.text_input("Please input user address." , key="g")
        my_dist = gmaps.distance_matrix(user_input,StreetAd)['rows'][0]['elements'][0]["distance"]["text"] # api calling distance
        my_dist2 = gmaps.distance_matrix(user_input,StreetAd)['rows'][0]['elements'][0]["distance"]["value"] #
        my_dur = gmaps.distance_matrix(user_input, StreetAd)['rows'][0]['elements'][0]["duration"]["text"]# api calling duration

        for values in my_dist:
                if my_dist2 >= 1000 and my_dist2 < 15000:
                        st.write("The closest Community League for ",Program, " is ",Comm,"and it is ", values, " away. The duration is: ", my_dur,".\n") #destinaton output 
        
                   
                

if __name__== "__main__":

        database()
