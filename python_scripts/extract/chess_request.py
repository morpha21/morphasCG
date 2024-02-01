"""
this module only provides functions to request data from a chess API
"""


import requests as rq
import pandas as pd
from json_normalize import json_normalize

def request_games(year: int, month: int, user: str, email: str) -> dict:
	"""gets chess data from chess.com"""
	year  = str(year)
	month = ("0"+str(month))[-2:]
	url   = f"https://api.chess.com/pub/player/{user}/games/{year}/{month}"
	print("requesting game data... ")
	headers = {'User-Agent': email}
	response = rq.get(url, headers=headers)

	if response.status_code == 200:
		game_json = response.json()
		df = pd.DataFrame(list(json_normalize(game_json)))
		print("done.\n")
		return df
	else:
		print(f'Error: {response.status_code}')
		return None














