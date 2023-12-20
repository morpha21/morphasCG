# Morpha's Chess Games

My aim in this project is to hone my skills in ETL processes. I intend to do it by 
automating a data pipeline that collects data from all my chess games (initially from 
chess.com's API, with plans to collect data from lichess.org's API too), processess them 
and loads them to some database.

I'm planning to use at least the following tools to do it:

- MySQL (on a container) 
- Docker 
- Docker-compose 
- AirFlow 
- Python

I may or may not use more tools in the future, or fewer tools, or substitute some of them 
for more adequate alternatives as I gain more knowledge.

## Current status: 
- collect.py makes a requisition to chess.com's API and turns it into a Pandas DataFrame.
- there's a docker-compose.yaml and a Dockerfile to set up a MySQL database, getting environment variables from not committed .env file. 
