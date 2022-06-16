import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.chky9yrkstez.us-east-1.rds.amazonaws.com",
  user="admin",
  password="adminmysql"
)

mycursor = mydb.cursor()
mycursor.execute("show databases")
a = mycursor.fetchall()
print(a)

