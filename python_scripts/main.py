import pandas as pd

from extract.chess_request import get_games
from json_normalize import json_normalize

email    = 'your_email@example.com'
url      = "https://api.chess.com/pub/player/morpha_21/games/2023/08"

game_json = get_games(url, email)['games']

df        = pd.DataFrame(list(json_normalize(game_json)))

df.columns = [col.replace(".","_").replace("@","") for col in df.columns]



print(df)
