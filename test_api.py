import numpy as np
import requests
import json
y_predict = requests.post('http://127.0.0.1:12345/predict', json=[{"pickup_community_area":40, "trip_start_hour":12,"trip_miles":1.3, "trip_seconds":100,"dropoff_community_area":33}],headers={"Content-Type": "application/json"},)
print(y_predict.json())
# Make array from the list
y_predict = np.array(y_predict.json())
print("The Fare Price is ", y_predict)