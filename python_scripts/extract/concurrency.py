import concurrent.futures
from datetime import datetime

from pandas import concat


from extract.chess_request import request_games


def worker(year_,user_, start_date, end_date):
	df_list = []

	for month in range(1, 13):
		if (year_ == start_date.year) and (month < start_date.month):
			continue

		df = request_games(year_, month, user_)
		df_list += [df]
		
		if (year_ == end_date.year) and (month == end_date.month):
			break
	return concat(df_list)


def execute(user, start_date, end_date):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for year in range(start_date.year, end_date.year+1):
                futures += [executor.submit(worker, year, user, start_date, end_date)]
        return [f.result() for f in futures]