# Morpha's Chess Games

My aim in this project is to hone my skills in ETL processes. I intend to do it by 
automating a data pipeline that collects data from all my chess games on chess.com.

The plan is:

1. to have a init.sh that sets everything up; 

2. a python software that checks for new games on chess.com, request new data, put it 
into a database, process it and save to another database.

3. A telegram bot that regularly sends some analytics to a number 

I'm planning to use at least the following tools to do it:

- MySQL (on a container)
- Docker
- Docker-compose
- AirFlow
- Python

I may or may not use more tools in the future, or fewer tools, or substitute some of them 
for more adequate alternatives as I gain more knowledge.


## Current status: 
- `data` directory is supposed to be the volume shared by host and containers - `mysql` 
contains data used by mysql container; - `mysql2` contains data used by mysql2 container; 
- `python_scripts` contains the ETL Python code, currently only able to get data from 
chess.com's API.
- `docker-compose.yml` is able to run containers, getting variables and ports from .env 
files.
