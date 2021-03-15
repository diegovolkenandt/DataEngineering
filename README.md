# Project: Data Modeling with Postgres

## This is the first project of the Udacity Data Engineering Nanodegree

This project consists of putting into practice the following concepts:

    - Data modeling woth PostGres
    - Creation of a Database star schema
    - Creating a ETL pipeline in Python

## Summary

This project has the purpose to create an SQL database, that serves the analytical purpose of a ficional music streaming service "Sparkify". Sparkify is interested in understanding, what songs users are listening to. Before the project start, there was no easy way to query data. The user activity data and song meta data only resides in JSON log files.

Therefore, this project consists in creating a PostGres database designed to optimize analytical queries on song play analysis.

    - Song datasets: all json files reside in subdirectories /data/song_data. 

    - Log datasets: all json files reside in subdirectories  /data/log_data.


## Database Schema

The schema used is the Star Schema with one main fact table songplay containing all the measures associated with each session of a user's song play, and four dimensional tables song, artist, users and time, each with a primary key that is being referenced from the fact table.

<img src="ERD-sparkifydb.png" alt="ERD Diagram">


We are using a Star Schema in this case ss our data model consists of only 5 tables, one fact table and 4 dimension tables. Star Schemas are also the simplest way of data mart schema and is the approach most widely used to develop data warehouses and dimensional data marts.


## Project structure

    / 
    - create_tables.py
    - etl.py
    - sql_queries.py
    - etl.ipynb
    - test.ipynb
    /data
        /log_data
        /song_data

#### create_tables.py
Resets and creates the database and the tables
    
#### sql_queries.py
Defines all SQL queries used in create_tables.py, etl.py and etl.ipynb
    
#### etl.ipynb
A Jupyter notebook, to analyse the data files and create test inserts

#### etl.py
The actual data pipeline
    
#### test.ipynb
Jupyter notebook to validate the if the data is correctly inserted


## How to Use
- Run create_tables.py from terminal to set up the database and tables.
- Run etl.py from terminal to process and load data into the database.
- Launch test.ipynb to run validation and example queries.
