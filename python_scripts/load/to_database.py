import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "morpha",
	password = "minhasenha",
	database = "chessdatabase")


mycursor = mydb.cursor()
mycursor.execute()
