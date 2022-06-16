import pandas as pd 
import requests
api_key="1cb8590dbf8618996e80b44c533047a1"

params = {
  'access_key': "YOUR_ACCESS_KEY"
}

params['access_key']=api_key
#api_result = requests.get('http://api.marketstack.com/v1/tickers/appl/eod',params)
api_result = requests.get('http://api.marketstack.com/v1/tickers/RELIANCE.XNSE/eod',params)
api_response = api_result.json()

new_df = pd.DataFrame.from_dict(api_response["data"]["eod"])
#new_df.to_csv("latest3.csv")
print(new_df)

dataframe = new_df[['open','high','low','close','volume','date']]
dataframe

dataframe["date"] = pd.to_datetime(dataframe["date"])
dataframe["date"].dt.date
dataframe["date"]=dataframe["date"].dt.date
dataframe


# MY_SQL_CONNECTIVITY CODE 
#import pymsql

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",auth_plugin='mysql_native_password'
)



#create a new database 
cur.mydb.cursor()
cur.execute("CREATE DATABASE stockmarket")
mydb.connect(database="stockmarket")


# using for loop to create multiple table 50 in db 

tablename=["a","b","c","d","e".....50]   #stocklist
i=0
while i<50:
    cur.execute("CREATE TABLE IF NOT EXISTS" + " " + tablename[i] +"(open varchar(250),high varchar(250),low varchar(250),close varchar(250),volume varchar(250),date DATE PRIMARY KEY)")
    i=i+1


#using for loop to insert data into table 

val = [
  ('Peter', 'Lowstreet 4'),   # convert the dataframe in such type of format
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21')
]


stocklist =["sbi ","itc"...50]

i=0
while i <50:
    sql = "INSERT INTO stocks (open,high,low,close,volume,date) VALUES (%s, %s,%s, %s,%s,%s)"
    cur.execute(sql,val[i])    #val will insert data into table 
    i=i+1

print(mydb)


# # Create cursor
# cur = mydb.cursor()

# # Execute Query
# mydb.execute("SELECT * from book_details")

# # Fetch the records
# result = mydb.fetchall()


