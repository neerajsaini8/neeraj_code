#using for loop to insert data into table 

val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21')
]

i=0
while i <3:
    sql = "INSERT INTO stocks (open, low) VALUES (%s, %s)"
    cur.execute(sql,val[i])
    i=i+1



# using for loop to create multiple table 50 in db 

tablename=["a","b","c","d","e"]
i=0
while i<5:
    cur.execute("CREATE TABLE IF NOT EXISTS" + " " + tablename[i] +"(open varchar(250),low varchar(250))")
    i=i+1
