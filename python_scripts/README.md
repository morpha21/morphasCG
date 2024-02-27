# Python Scripts

Currently, the `load_to_csv.py` script is able to generate a `.csv` file with all matches from a given player in a given period of time. 
It is supposed to be used like this: 

```$ python load_to_csv.py <user_name> <start_date> <end_date>```

Where

- `<user_name>` is the username of the player on chess.com;
- `<start_date>` and `<end_date>` are dates in the format "YYYY/mm".

Both `<start_date>` and `<end_date>` are optional. If not specified, `<start_date>` will be considered as "2015/01", and `<end_date>` will considered as the current month.
If only one date is provided as an argument, then it will be considered as `<start_date>`. 

`load_to_csv.py` will then make concurrent requests to chess.com's API, using functions defined in `extract` package to do the requests, build a <b>Pandas DataFrame</b>, 
and use functions defined in `transform` package to make it look like a dataset in which each chess match is from the provided player. 


## to do:
- Soon the csv file built by `load_to_csv.py` will contain information about the country from which the opponent is from. 
- implement the option of loading data to an SQL database instead of csv file.
- implement the option of generating more than one type of dataset.
- implement the option of just appending data to a dataset (be it at a csv file or at a actual database).
- a Jupyter Notebook with a Exploratory Data Analysis of data. 
