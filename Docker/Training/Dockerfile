FROM python:3.9
COPY . /usr/app/
WORKDIR /usr/app/
RUN pip install -r requirements.txt
RUN python test_train_split.py TaxiData.tsv
RUN python data_analysis.py TaxiData_train.csv
RUN python data_analysis.py TaxiData_test.csv
RUN python train_gbr.py TaxiData_train_Processed.csv
RUN python train_xgb.py TaxiData_train_Processed.csv
RUN python evaluate.py TaxiData_test_Processed.csv gbrmodel.pkl xgbmodel.pkl