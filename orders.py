

#extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


#read data from the file and checking first 20 rows
import pandas as pd
df = pd.read_csv('orders.csv')
df.head(20) 


#checking unique values in Ship mode column
df['Ship Mode'].unique()

#handling null values
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df

#rename columns names ..make them lower case and replace space with underscore
df.rename(columns={'Order Id':'order_id', 'City':'city'}) # In this we have to write all the columns name i.e why 
df.columns #gives all the columns
df.columns=df.columns.str.lower() #it will convert the columns into lower case
df.columns=df.columns.str.replace(' ','_') #it wil convert the space into _
df.head(5)

#derive new columns discount , sale price and profit
df['discount']=df['list_price']*df['discount_percent']*.01  #this 01 is 1/100
df['sale_price']= df['list_price']-df['discount'] 
df['profit']=df['sale_price']-df['cost_price']
df


#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
df.dtypes

#drop cost price list price and discount percent columns
#we are using inplace to change data directly or to change real data
#suppose we don't use inplace then when we view real data there are no columns deleted
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)  
df

import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="masters"
)
print(mydb)

!pip install mysql-connector-python pandas sqlalchemy pymysql kaggle


from sqlalchemy import create_engine

# Create a SQLAlchemy engine
engine = create_engine('mysql+pymysql://root:12345@127.0.0.1:3306/masters')

# Load the data into the SQL table using the 'replace' option
df.to_sql('df_orders', con=engine, index=False, if_exists='append')

print("Data loaded successfully into MySQL database.")
