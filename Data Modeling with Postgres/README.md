# Data Modeling with Postgres

## Purpose of the database

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. 
The purpose of the project is to create a data pipeline to convert song data and log data into information about songs and store in Postgre database named "sparkifydb", which analytics team can exact data directly from the database.

## Database Schema

This database use a star schema optimized for queries on song play analysis. This includes the following tables:

#### Fact Table
* songplays - records in log data associated with song plays i.e. records with page NextSong
* songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### Dimension Tables
* users - users in the app
* user_id, first_name, last_name, gender, level
* songs - songs in music database
* song_id, title, artist_id, year, duration
* artists - artists in music database
* artist_id, name, location, lattitude, longitude
* time - timestamps of records in songplays broken down into specific units
* start_time, hour, day, week, month, year, weekday

## Prerequisites

* Python >= 3.0

* psycopg2 >= 2.0

## How to run the ETL pipeline

First run create_tables.py, it will create database and tables needed. 

```
python3 create_tables.py
```

Then run etl.py, it will convert data from data folder into database.

```
python3 etl.py
```

## File Structure

* data folder: contains data used to build the database
* etl.py: data pipeline
* sql_queries.py: store queries used to extract data
* creat_tables.py: Create the database and required tables.