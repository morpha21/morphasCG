import pandas as pd

def format_columns(columns: pd.core.indexes.base.Index) -> list:
	"""receives thecolumns of a DataFrame and returns a list with more suitable
	column names"""
	return [col.replace(".","_").replace("@","") for col in columns]


columns_to_be_dropped = ['initial_setup', 'rated', 'rules', 'white_id', 'black_id',
			   'start_time']


def adequate(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
	df.columns = format_columns(df.columns)
	return df.drop(columns_to_be_dropped, axis=1)
