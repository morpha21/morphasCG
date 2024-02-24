"""
this module only provides functions to request data from a chess API
"""


import requests as rq
import pandas as pd
from json_normalize import json_normalize

def request_games(year: int, month: int, user: str, email: str) -> pd.core.frame.DataFrame:
	"""gets chess data from chess.com"""
	year  = str(year)
	month = ("0"+str(month))[-2:]
	url   = f"https://api.chess.com/pub/player/{user}/games/{year}/{month}"
	print(f"\rrequesting game data from {month}/{year}... ", end=' ')
	headers = {'User-Agent': email}
	response = rq.get(url, headers=headers)
	while response.status_code == 429:
		response = rq.get(url, headers=headers)
	if response.status_code == 200:
		game_json = response.json()
		df = pd.DataFrame(list(json_normalize(game_json)))
		return df
	print(f'Error: {response.status_code}')
	return None



def get_user(user: str, email:str) -> pd.core.frame.DataFrame:
	"""gets data from a given chess.com user"""
	url= f"https://api.chess.com/pub/player/{user}/stats"
	headers = {'User-Agent': email}
	response = rq.get(url, headers=headers)
	if response.status_code == 200:
		user_json = response.json()
		disposable_keys = [el for el in ['tactics', 'puzzle_rush'] if el in  user_json.keys()]
		for key in disposable_keys:
			del user_json[key]
		return pd.DataFrame(list(json_normalize(user_json)))
	else:
		print(f'Error: {response.status_code}')
		return None











