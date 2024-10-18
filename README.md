TaxiData.csv - Input Data
test_train_split.py -> for splitting Testing and Training Data.

data_analysis.py -> For pre-processing the data.

train_gbr.py -> Training a GBR model

train_xgb.py -> Training XGB model

evaluate.py -> Picking the best model between XGB and GBR model.

deploy.py -> Deploying the model

test_api.py -> Testing the API

webapp_Taxi.py -> Deploying the Web application.

TaxiData_Train.csv -> Training Data

Run pipeline.cmd command to run the model pre-processing, training, evaluation and deployment using flask.

For testing the app, run python test_api.py command

For running the webapp, run "streamlit run webapp_Taxi.py"

For running the service, use python deploy.py command.
Test using curl HTTP://127.0.0.1:12345/show_result -> shows the default prediction.
In postman, set Headers -> Content-Type : application/json
Input:
[{"pickup_community_area":40, "trip_start_hour":12,"trip_miles":20.3, "trip_seconds":5000,"dropoff_community_area":33},{"pickup_community_area":40, "trip_start_hour":12,"trip_miles":20.3, "trip_seconds":500,"dropoff_community_area":33}]
