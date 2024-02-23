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

	if response.status_code == 200:
		game_json = response.json()
		df = pd.DataFrame(list(json_normalize(game_json)))
		return df
	else:
		print(f'Error: {response.status_code}')
		return None














