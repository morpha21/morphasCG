import pandas as pd
import requests as rq
from json_normalize import json_normalize

def get_chess_data(url, email):
  """gets chess data from chess.com"""
  headers = {'User-Agent': email}
  response = rq.get(url, headers=headers)

  if response.status_code == 200:
    return response.json()
  else:
    print(f'Error: {response.status_code}')
    return None

email = 'your_email@example.com'
url   = "https://api.chess.com/pub/player/morpha_21/games/2023/08"

# importa uma lista de jogos (json)
# cada jogo vem como dicionário
raw_data = get_chess_data(url, email)['games']

df = pd.DataFrame(list(json_normalize(raw_data)))

columns = []
for col in df.columns:
  if "." in col:
    col = col.replace(".", "_")
  if "@" in col:
    col = col.replace("@", "")
  columns.append(col)
df.columns = columns
