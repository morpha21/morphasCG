import mysql.connector

from pandas import DataFrame

def connect(df, host_name, user_name, user_password, db_name):
	mydb = mysql.connector.connect(
		host = host_name,
		user = user_name,
		password = user_password,
		database = db_name)
	mycursor = mydb.cursor()
	mycursor.execute()

	query = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"

	for column in df.columns:
	
	mycursor.execute()



if __name__ == "main":
	host     = args[0]
	user     = args[1]
	password = args[2]
	database = args[3]
