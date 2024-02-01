import mysql.connector

from pandas import DataFrame

def connect(df: DataFrame, host_name: str, user_name: str, user_password: str, db_name: str):
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
