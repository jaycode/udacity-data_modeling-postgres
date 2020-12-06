# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL,
        start_time time not null,
        user_id int not null,
        level varchar,
        song_id varchar,
        artist_id varchar,
        session_id int not null,
        location varchar,
        user_agent text,
        PRIMARY KEY (songplay_id));
""")

user_table_create = ("""
    CREATE TABLE users(
        user_id int,
        first_name varchar,
        last_name varchar,
        gender varchar,
        level varchar,
        PRIMARY KEY (user_id));
""")

song_table_create = ("""
    CREATE TABLE songs(
        song_id varchar,
        title varchar not null,
        artist_id varchar not null,
        year int,
        duration float,
        PRIMARY KEY (song_id));
""")

artist_table_create = ("""
    CREATE TABLE artists(
        artist_id varchar,
        name varchar not null,
        location varchar,
        latitude float,
        longitude float,
        PRIMARY KEY (artist_id));
""")

time_table_create = ("""
    CREATE TABLE time(
        start_time time,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int,
        PRIMARY KEY (start_time));
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays(
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE set level = EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

# case 1: Select by song, artist, and duration
# song_select = ("""
#     SELECT s.song_id, s.artist_id
#     FROM songs s
#         INNER JOIN artists a ON s.artist_id = a.artist_id
#     WHERE s.title = %s AND a.name = %s AND s.duration = %s;
# """)

# case 2: Select by song and artist
# song_select = ("""
#     SELECT s.song_id, s.artist_id
#     FROM songs s
#         INNER JOIN artists a ON s.artist_id = a.artist_id
#     WHERE s.title = %s AND a.name = %s;
# """)

# case 3: Select by song
# song_select = ("""
#     SELECT s.song_id
#     FROM songs s
#     WHERE s.title = %s;
# """)

# case 4: Select by artist
# song_select = ("""
#     SELECT a.artist_id
#     FROM artists a
#     WHERE a.name = %s;
# """)

# case 5:
song_select = ("""
SELECT s.song_id,a.artist_id
FROM songs s JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = %s AND
a.name = %s AND
s.duration = %s
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
