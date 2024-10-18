## This program takes the Taxi Data, Pre-processes it and generates the processed file
import sys
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import pandas as pd
 
input_filepath= sys.argv[1]
processed_path=(input_filepath.split("."))[0]
print(processed_path)
processed_filepath =processed_path+'_Processed.csv'
dataframe=pd.read_csv(input_filepath)

# label_encoder object knows  
# how to understand word labels. 
#label_encoder = preprocessing.LabelEncoder()
#dataframe['company']= label_encoder.fit_transform(dataframe['company'])
#dataframe['payment_type']= label_encoder.fit_transform(dataframe['payment_type'])

# Convert pickup_community_area and dropoff_community_area as categorical variable
#dataframe['pickup_community_area']= label_encoder.fit_transform(dataframe['pickup_community_area'])
#dataframe['dropoff_community_area']= label_encoder.fit_transform(dataframe['dropoff_community_area'])

# Remove un-used columns after analysis
df = dataframe.drop(['trip_start_timestamp','trip_start_day','trip_start_month','pickup_census_tract',
              'dropoff_census_tract','payment_type','tips','dropoff_latitude','pickup_latitude', 'dropoff_longitude', 'pickup_longitude', 'company'], axis=1)

#Drop NA rows
df = df.dropna()
col =['pickup_community_area','trip_start_hour','trip_miles','company','trip_seconds','dropoff_community_area','fare']
#scaler = StandardScaler()

#df_scaled = pd.DataFrame(scaler.fit_transform(df[col]),columns = col)

df.to_csv(processed_filepath)
