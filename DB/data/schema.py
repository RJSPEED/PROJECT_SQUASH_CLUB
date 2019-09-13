import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "GroveSquash.db"
DBPATH = os.path.join(DIR, DBFILENAME)


def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename="users"))

        SQL = """CREATE TABLE users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(30) NOT NULL,
            password_hash VARCHAR(128),
            first_name VARCHAR(15) NOT NULL,
            last_name VARCHAR(15) NOT NULL,
            phone_1 VARCHAR(15) NOT NULL,
            phone_2 VARCHAR(15),
            membership_type NOT NULL,
            membership_fee,
            profile NOT NULL
            );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="comps"))

        SQL = """CREATE TABLE comps(
            comp_id INTEGER NOT NULL,
            comp_name VARCHAR(100) NOT NULL,
            sub_comp_id INTEGER NOT NULL,
            sub_comp_name VARCHAR(100) NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            league BOOLEAN ,
            PRIMARY KEY(comp_id, sub_comp_id)
             );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="comp_participants"))

        SQL = """CREATE TABLE comp_participants(
            comp_id INTEGER NOT NULL,
            sub_comp_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            points INTEGER,
            PRIMARY KEY(comp_id, sub_comp_id, user_id),
            FOREIGN KEY(comp_id, sub_comp_id) REFERENCES comps(comp_id, sub_comp_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
            );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="matches"))

        SQL = """CREATE TABLE matches(
            comp_id INTEGER NOT NULL,
            sub_comp_id INTEGER NOT NULL,
            match_id INTEGER NOT NULL,
            p1_user_id INTEGER NOT NULL,
            p2_user_id INTEGER NOT NULL,
            walkover BOOLEAN,
            date_played DATE,
            p1_games_won INTEGER NOT NULL,
            p2_games_won INTEGER NOT NULL,
            p1_g1_score INTEGER,
            p2_g1_score INTEGER,
            p1_g2_score INTEGER,
            p2_g2_score INTEGER,
            p1_g3_score INTEGER,
            p2_g3_score INTEGER,
            p1_g4_score INTEGER,
            p2_g4_score INTEGER,
            p1_g5_score INTEGER,
            p2_g5_score INTEGER,
            PRIMARY KEY(comp_id, sub_comp_id, match_id),
            FOREIGN KEY(comp_id, sub_comp_id) REFERENCES comps(comp_id, sub_comp_id)
            );"""

        cur.execute(SQL)

    