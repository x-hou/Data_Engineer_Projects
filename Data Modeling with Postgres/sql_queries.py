# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
songplay_id serial, 
start_time timestamp NOT NULL, 
user_id varchar NOT NULL, 
level varchar, 
song_id varchar, 
artist_id varchar, 
session_id varchar, 
location varchar, 
user_agent varchar
);
""")
# 

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id varchar NOT NULL PRIMARY KEY, 
first_name varchar, 
last_name varchar, 
gender varchar, 
level varchar
);
""")
 
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id varchar UNIQUE PRIMARY KEY, 
title varchar, 
artist_id varchar, 
year int, 
duration float
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id varchar UNIQUE PRIMARY KEY, 
name varchar, 
location varchar, 
lattitude float, 
longitude float
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time timestamp NOT NULL PRIMARY KEY, 
hour float, 
day int, 
week int, 
month int, 
year int, 
weekday int
);
""")

add_foreign_key_1 = ("""ALTER TABLE songplays ADD CONSTRAINT fk1 FOREIGN KEY (start_time) REFERENCES time (start_time);
""")
add_foreign_key_2 = ("""ALTER TABLE songplays ADD CONSTRAINT fk2 FOREIGN KEY (user_id) REFERENCES users (user_id);
""")
add_foreign_key_3 = ("""ALTER TABLE songplays ADD CONSTRAINT fk3 FOREIGN KEY (artist_id) REFERENCES artists (artist_id);
""")
add_foreign_key_4 = ("""ALTER TABLE songplays ADD CONSTRAINT fk4 FOREIGN KEY (song_id) REFERENCES songs (song_id);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)  on conflict(user_id) do update set level=excluded.level;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) on conflict do nothing;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s) on conflict do nothing;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) on conflict do nothing;
""")

# FIND SONGS
#  find the song ID and artist ID based on the title, artist name, and duration of a song
song_select = ("""SELECT songs.song_id, songs.artist_id FROM songs, artists WHERE artists.artist_id = songs.artist_id AND songs.title = %s AND artists.name = %s AND songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create, add_foreign_key_1, add_foreign_key_2, add_foreign_key_3, add_foreign_key_4]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]