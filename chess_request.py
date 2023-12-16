"""

this module only provides functions to request data from a chess API

"""

import requests as rq


def get_games(url, email):
  """gets chess data from chess.com"""
  print("requesting game data... ")
  headers = {'User-Agent': email}
  response = rq.get(url, headers=headers)

  if response.status_code == 200:
    print("done.\n")
    return response.json()
  else:
    print(f'Error: {response.status_code}')
    return None





