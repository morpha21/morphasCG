import pandas as pd
from json_normalize import json_normalize


from extract.chess_request import get_games
import transform.chess_transform as ct


# maybe getting user from file?
# dates as arguments?


with open(".email", 'r') as email_file:
	url	  = "https://api.chess.com/pub/player/morpha_21/games/2023/08"
	email	  = email_file.read().strip()
	game_json = get_games(url, email)['games']
	df        = pd.DataFrame(list(json_normalize(game_json)))


df = ct.adequate(df)

for i in df.columns:
	print(i)

print()
print(df.iloc[:, 15:20])





