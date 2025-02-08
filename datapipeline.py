#importing libraries
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder,StandardScaler


# PIPELINE OF DATA

# STEP 1 : EXTRACT
# LOAD THE DATA FROM CSV FILE(encoding set  to handle special characters)

data = pd.read_csv(r"C:\Users\mamun\Downloads\Diwali Sales Data - Diwali Sales Data.csv",encoding='latin1')
print(data.head())


# STEP 2:TRANSFORM
# preprocessing the dataset to make it useable for analysis

# REMOVE UNNECESSARY columns
data = data.drop(columns=['Status','unnamed1','Age Group','User_ID','Cust_name'],errors = 'ignore')


# FIND THE SHAPE OF DATASET
print("SHAPE OF DATASET:",data.shape)


# MISSING VALUES IN DATASET
print("MISSING VALUES IN DATASET:")
print(data.isna().sum())

# FILL MISSING VALUES USING SIMPLE IMPUTER
imputer = SimpleImputer(strategy='mean')
data['Amount']=imputer.fit_transform(data[['Amount']])


# HANDLING OUTLIERS USING CLIPPING
data['Amount']=data['Amount'].clip(lower=data['Amount'].quantile(0.05),upper=data['Amount'].quantile(0.95))


# LABEL ENCODING(for gender)
le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])

# FEATURE ENGINEERING
data['Total_Spend']=data['Amount']*data['Orders']
data['Avg_Spend_per_Order']=data['Total_Spend']/data['Orders']

# CATEGORIZING CUSTOMERS BASED ON NUMBERS OF ORDERS
data['Order_frequency'] = pd.qcut(data['Orders'],q=4,labels=['low','medium','high','very high'])



# AGGREGATE DATA(Example:total sales per category)
category_sales = data.groupby('Product_Category').agg({'Amount':'sum'}).reset_index()
category_sales.columns = ['Product_Category','Total_Sales']


# MERGE AGGREGATED DATA BACK INTO MAIN DATAFRAME
data = data.merge(category_sales,on='Product_Category',how='left')


# CREATING HIGH VALUE CUSTOMER FLAG(TOP 25 % SPENDERS)
data['High_Value_Customer'] = data['Total_Spend'] > data['Total_Spend'].quantile(0.75)

#STEP 3 : LOAD
#SAVE THE CLEANED AND TRANSFORMED DATA
data.to_csv(r"C:\Users\mamun\OneDrive\Documents\cleaned_diwali_sales_data.csv",index=False)

# DISPLAY TRANSFORMED DATA
print("\nTRANSFORMED DATA :")
print(data.head())

print("ETL process completed sucessfully .Transformed data saved as 'cleaned_diwali_sales_data.csv'")
