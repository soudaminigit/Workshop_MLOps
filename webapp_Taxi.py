import streamlit as st
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import urllib.request
st.set_option('deprecation.showfileUploaderEncoding', False)
import requests
import json


def predict_fare(pickup_community_area , trip_start_hour,trip_miles,trip_seconds, dropoff_community_area):
    y_predict = requests.post('http://127.0.0.1:12345/predict',   json=[{"pickup_community_area":pickup_community_area, "trip_start_hour":trip_start_hour,"trip_miles":trip_miles, "trip_seconds":trip_seconds,"dropoff_community_area":dropoff_community_area}],headers={"Content-Type": "application/json"},)
    print(y_predict.json())
    # Make array from the list
    y_predict = np.array(y_predict.json())
    print("The Fare Price is ", y_predict)
    return y_predict

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
      st.success('Fare price {}'.format(result))

    if st.button("About"):
      st.subheader("Running Model using Streamlit")

if __name__=='__main__':
  main()