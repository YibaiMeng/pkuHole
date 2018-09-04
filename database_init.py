# This program is to init the database used. It only needs to run once.

import sqlite3

sqlite_file = "data.sqlite"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

post_create = "CREATE TABLE IF NOT EXISTS post(pid integer PRIMARY KEY NOT NULL, time integer NOT NULL, type int NOT NULL, content text NOT NULL, url text, last_active integer, reply integer, like integer);"

comment_create = "CREATE TABLE IF NOT EXISTS comment(cid integer PRIMARY KEY NOT NULL, pid integer NOT NULL, time integer NOT NULL, user integer NOT NULL, content text NOT NULL);"
stat_create = "CREATE TABLE IF NOT EXISTS stat(time integer NOT NULL, pid integer NOT NULL, reply integer NOT NULL, like integer NOT NULL);"

c.execute(post_create)
c.execute(comment_create)
c.execute(stat_create)

conn.commit()
conn.close()





