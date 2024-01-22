import pandas as pd


from extract.chess_request import get_games
from json_normalize        import json_normalize



# maybe getting user from file?
# dates as arguments?


with open(".email", 'r') as email_file:
	url	  = "https://api.chess.com/pub/player/morpha_21/games/2023/08"
	email	  = email_file.read().strip()
	game_json = get_games(url, email)['games']
	df        = pd.DataFrame(list(json_normalize(game_json)))


df.columns = [col.replace(".","_").replace("@","") for col in df.columns]


a = df['rules'].unique()

print (a)
