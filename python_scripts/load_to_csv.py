from sys import argv
if len(argv) == 1:
	print("usage:")
	print("python load_to_csv <chess.com's player username> <start_date> <end_date>")
	print("")
	print("both <start_date> and <end_date> should in the format YYYY/mm")
	print("both <start_date> and <end_date> are optional with the following default values:")
	print("<start_date> = 2015/01")
	print("<end_date>   = current month")
	print("")
	print("If only one date is specified, it will be considered as <start_date>")
	exit()


import concurrent.futures
from datetime import datetime

import pandas as pd

import transform.chess_transform as ct
from extract.chess_request import request_games
from extract.chess_request import get_user


def worker(year_,user_):
	df_list = []
	global end_date
	global start_date

	for month in range(1, 13):
		if (year == start_date.year) and (month < start_date.month):
			continue

		df = request_games(year_, month, user_)
		df_list += [df]
		
		if (year_ == end_date.year) and (month == end_date.month):
			break
	return pd.concat(df_list)


user       = argv[1]
start_date = datetime.strptime(argv[2], "%Y/%m") if len(argv) > 2 else datetime(2015, 1, 1)
end_date = datetime.strptime(argv[3], "%Y/%m") if len(argv) > 3 else datetime.now()



with concurrent.futures.ThreadPoolExecutor() as executor:
	futures = []
	for year in range(start_date.year, end_date.year+1):
			futures += [executor.submit(worker, year, user)]
	df_list = [f.result() for f in futures]

df = pd.concat(df_list)
df = ct.adequate(df)

user = (
	df['white_username'][0]
	if df['white_username'][0].lower() == user.lower()
	else df['black_username'][0]
	)


df.sort_index(inplace=True)

if len(df[df['black_username'] == user]['black_uuid'].unique()) > 0:
	uuid = df[df['black_username'] == user]['black_uuid'].unique()[0]

df   = ct.personalize(df, user)

print()
print(df)
df.to_csv(f"{user}_chess_games.csv")



l = 1 + len(df['opponent'])//6

opponent_batches = [df['opponent'][l*i:l*(i+1)] for i in range(0,7)]









df.to_csv(f"{user}_chess_games.csv")


