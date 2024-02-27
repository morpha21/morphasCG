# Morpha's Chess Games

The idea here is to extract chess data from an API, process, and store it to a database. 

Currently, the Python code inside `python_scripts` directory is able to make concurrent requests
to chess.com's API and process the data to save it to a CSV file. For more details, check README
file inside. 

The `infrastructure` directory contains code relative to SQL databases on Docker containers, using
Dockercompose, where I want to store the data. The usage of containers here are mostly for ease
of use for prototyping and will possibly be replaced in the future.

