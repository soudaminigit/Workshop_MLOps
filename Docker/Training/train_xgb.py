from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error,r2_score
import sys

import joblib
import pandas as pd

def hyperparameter_tuning(param_grid, model,model_name,X_train,y_train, X_test, y_test,model_path):
    # Perform grid search with cross-validation 
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    # Get the best hyperparameters 
    best_params = grid_search.best_params_
    print(f"Best Hyperparameters for {model_name}:", best_params)

    # Get the best model
    print(f"Best model estimator in the {model_name}")
    
    best_model = grid_search.best_estimator_

    # Evaluate the best model on the test data
    test_predictions = best_model.predict(X_test)

    mse = mean_squared_error(y_test, test_predictions)
    print("Mean Squared Error:", mse)
    r = r2_score(y_test,test_predictions)
    print("R2_Score",r)
    model_file=model_name+".pkl"
    best_model.fit(X_train,y_train)
    joblib.dump(best_model, model_path)

#Initialize variables
processed_filepath=sys.argv[1]
model_path='xgbmodel.pkl'
model_columns_path='model_columns.pkl'
col =['pickup_community_area','trip_start_hour','trip_miles','trip_seconds','dropoff_community_area']

df=pd.read_csv(processed_filepath)
df_scaled=df[col]
y=df['fare']
X_train,X_test,y_train,y_test = train_test_split(df_scaled,y,test_size=0.1)
param_grid_xgb = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.001, 0.05,0.01, 0.1, 0.5],
    'max_depth': [3,7,11,15]
}
# Initialize the XGBRegressor model
model_xgb = XGBRegressor()
joblib.dump(col,model_columns_path)
hyperparameter_tuning(param_grid_xgb,model_xgb,"Xgboost",X_train,y_train,X_test, y_test,model_path)