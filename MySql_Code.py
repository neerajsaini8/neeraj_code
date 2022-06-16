# MY_SQL_CONNECTIVITY CODE 
#import pymsql

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",auth_plugin='mysql_native_password'
)

print(mydb)


# # Create cursor
# cur = mydb.cursor()

# # Execute Query
# mydb.execute("SELECT * from book_details")

# # Fetch the records
# result = mydb.fetchall()