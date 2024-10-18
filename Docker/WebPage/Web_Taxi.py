import streamlit as st
from PIL import Image
import pickle
import numpy as np
import pandas as pd
import urllib.request
st.set_option('deprecation.showfileUploaderEncoding', False)
import requests
import json
import joblib


def predict_fare(pickup_community_area , trip_start_hour,trip_miles,trip_seconds, dropoff_community_area):

    model_file= 'model.pkl'
    model_columns_file = 'model_columns.pkl'
    model = joblib.load(model_file)
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')
    print(model_columns)
    prediction = [15.5]
    if model:
        try:
            data=[[pickup_community_area , trip_start_hour,trip_miles,trip_seconds, dropoff_community_area]]
            query = pd.DataFrame(data,columns=['pickup_community_area' , 'trip_start_hour','trip_miles','trip_seconds', 'dropoff_community_area'])
            print(query)
            query = query.reindex(columns=model_columns)
            #query = transform(query)
            print(query)	
            prediction = model.predict(query)
            print(prediction)
            return prediction[0]

        except:

            print("error in loading the model")
    else:
        print ('Train the model first')
        return ('No model here to use')
        return 0

    
  

def main():

    html_temp = """
   <div class="" style="background-color:White;" >
   <div class="clearfix">
   <div class="col-md-12">
   <center><p style="font-size:40px;color:black;margin-top:10px;">Taxi Fare Prediction Service</p></center>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Fare Prediction")

    pickup_community_area = st.number_input("pickup Community Area Code")
    trip_start_hour= st.number_input("Trip Start Hour",0,23)
    trip_miles = st.number_input("Trip Miles",1,500)
    trip_seconds = st.number_input("Trip Seconds")
    dropoff_community_area = st.number_input("dropoff Community Area Code")
 

    result=""
    if st.button("Predict"):
      result=predict_fare(pickup_community_area , trip_start_hour,trip_miles,trip_seconds, dropoff_community_area)
      st.success('Fare price {} $'.format(result))

    if st.button("About"):
      st.subheader("Running Model using Streamlit")

if __name__=='__main__':
  main()