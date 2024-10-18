# Split the Data into Testing and Training data
python testtrainsplit.py TaxiData.csv
python Data_analysis.py TaxiData_train.csv
python Data_analysis.py TaxiData_test.csv
python train_gbr.py TaxiData_train_Processed.csv
python train_xgb.py TaxiData_train_Processed.csv
python evaluate.py TaxiData_test_Processed.csv gbrmodel.pkl xgbmodel.pkl
python deploy.py
python test_api.py