from datetime import datetime
import pandas as pd

from extract.chess_request import request_games
import transform.chess_transform as ct


current_year = datetime.now().year
current_month = datetime.now().month
user  = "morpha_21"
email = ""


with open("extract/.email", 'r') as email_file:
	email = email_file.read().strip()


df_list = []

for year in range(2023, current_year+1):
	for month in range(1, 13):
		df = request_games(year, month, user, email)
		df_list += [df]
		if (year == current_year) and (month == current_month):
			break

df = pd.concat(df_list)
df = ct.adequate(df)
df.sort_index(inplace=True)

uuid = df[df['white_username'] == user]['white_uuid'].unique()[0]


df = ct.personalize(df, user)




print("\nColumns:")
for i in df.columns:
	print(i)

print()
print(df)





