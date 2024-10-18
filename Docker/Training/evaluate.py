from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error,r2_score
import sys

import joblib
import pandas as pd


#Initialize variables
processed_filepath=sys.argv[1]
print(processed_filepath)
model1_path= sys.argv[2]
print("Model 1:")
print(model1_path)
model2_path = sys.argv[3]
print("Model 2:")
print(model2_path)
final_model_path = 'model.pkl'
model_columns_path = 'model_columns.pkl'
col =joblib.load(model_columns_path)

df=pd.read_csv(processed_filepath)
df_test=df[col]
y=df['fare']
model1 = joblib.load(model1_path)
test_prediction1 = model1.predict(df_test)
mse1 = mean_squared_error(y, test_prediction1)
print("Mean Squared Error for Model1:", mse1)
r1 = r2_score(y,test_prediction1)
print("R2_Score for Model1 ",r1)
if((mse1>20)&(r1<0.5)):
    print("Model1 quality doesnt meet the bar. Re-train the model")
    exit;

model2 = joblib.load(model2_path)
test_prediction2 = model2.predict(df_test)
mse2 = mean_squared_error(y, test_prediction2)
print("Mean Squared Error Model 2:", mse2)
r2 = r2_score(y,test_prediction2)
print("R2_Score Model 2",r2)
if((mse2>20)&(r2<0.5)):
    print("Model 2 quality doesn't meet the bar. Re-train the model")
    exit;

if(r1 > r2):
    print("Model 1 is best model")
    joblib.dump(model1, final_model_path)
else :
    print("Model 2 is the best model")
    joblib.dump(model2, final_model_path)
print("Final model saved to model.pkl")
