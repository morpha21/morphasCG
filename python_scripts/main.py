import pandas as pd


from extract.chess_request import request_games
import transform.chess_transform as ct

year  = 2024
month = 1
user  = "morpha_21"
email = ""


with open("extract/.email", 'r') as email_file:
	email = email_file.read().strip()


df = request_games(year, month, user, email)
df = ct.adequate(df)

for i in df.columns:
	print(i)

print()
print(df)





