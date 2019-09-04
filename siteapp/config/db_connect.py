import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="pass",
	database="mydatabase"
	)
