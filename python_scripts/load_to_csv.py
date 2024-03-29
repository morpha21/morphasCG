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


from extract.concurrency import worker
from extract.concurrency import execute




user       = argv[1]
start_date = datetime.strptime(argv[2], "%Y/%m") if len(argv) > 2 else datetime(2015, 1, 1)
end_date = datetime.strptime(argv[3], "%Y/%m") if len(argv) > 3 else datetime.now()


df_list = execute(user, start_date, end_date)

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


# l = 1 + len(df['opponent'].unique())//6

# opponent_batches = [df['opponent'].unique()[l*i:l*(i+1)] for i in range(0,6)]

# print()

# for i in opponent_batches:
# 	print(len(i))
# 	print(i[0:6])
# 	print()

print(f"total: {len(df.opponent.unique())}")
df.to_csv(f"{user}_chess_games.csv")
