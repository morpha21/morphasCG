import pandas as pd

from chess_request import get_games
from json_normalize import json_normalize

email    = 'your_email@example.com'
url      = "https://api.chess.com/pub/player/morpha_21/games/2023/08"

game_json = get_games(url, email)['games']
df        = pd.DataFrame(list(json_normalize(game_json)))
columns   = []

for col in df.columns:
  if "." in col:
    col = col.replace(".", "_")
  if "@" in col:
    col = col.replace("@", "")
  columns.append(col)
df.columns = columns


print(df)
