# DROP TABLES


songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES


songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplay (
        songplay_id bigserial PRIMARY KEY,
        start_time timestamp NOT NULL,
        user_id int,
        level varchar,
        song_id varchar,
        artist_id varchar,
        session_id int NOT NULL,
        location varchar,
        user_agent varchar);
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id int PRIMARY KEY,
        first_name varchar,
        last_name varchar,
        gender varchar(1),
        level varchar);
""")


song_table_create = ("""
    CREATE TABLE IF NOT EXISTS song (
        song_id varchar PRIMARY KEY,
        title varchar,
        artist_id varchar,
        year int,
        duration numeric);
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artist (
        artist_id varchar PRIMARY KEY,
        name varchar,
        location varchar,
        latitude numeric(8, 6),
        longitude numeric(9, 6));
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time timestamp PRIMARY KEY,
        hour int NOT NULL,
        day int NOT NULL,
        week int NOT NULL,
        month int NOT NULL,
        year int NOT NULL,
        weekday varchar NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplay 
        (start_time, user_id,level, song_id, artist_id, session_id, location, user_agent)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = (""" 
    INSERT INTO users (user_id, first_name, last_name, gender, level)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (user_id)
        DO UPDATE
        SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO song (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (song_id)
        DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artist (artist_id, name, location, latitude, longitude) \
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (artist_id)
        DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (start_time)
        DO NOTHING;        
""")

# FIND SONGS

song_select = ("""
    SELECT song.song_id, song.artist_id 
        FROM song JOIN artist 
        ON song.artist_id = artist.artist_id \
        WHERE song.title = %s AND artist.name = %s AND song.duration = %s;
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]