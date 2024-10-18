import pandas as pd
text_file='TaxiData.csv'
train_file='TaxiData_train.csv'
test_file='TaxiData_test.csv'
ratio = 0.7
df = pd.read_csv(text_file) 
total_rows = df.shape[0]
train_size = int(total_rows*ratio)
 
# Split data into test and train
train = df[0:train_size]
df.to_csv(train_file)
test = df[train_size:]
df.to_csv(test_file)