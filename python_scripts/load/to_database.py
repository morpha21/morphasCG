import mysql.connector





with open('../../mysql.env', 'r') as file:
	content = file.read().split('\n')

with open('../../.env', 'r') as file:
	port = file.read().split('\n')[0].split('=')[1]

content = [c.split('=')[1] for c in content if c != '']


hostname = "localhost:"+port
db       = content[0]
user     = content[2]
password = content[3]



print (hostname)
print (db)
print (user)
print (password)


#mydb = mysql.connector.connect()
