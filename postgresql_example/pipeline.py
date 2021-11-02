'''Data Pipeline for moving sqlite db to postgres hosted db'''

import psycopg2
import sqlite3
from queries import *

# Connecting to PostgreSQL DB

dbname = "qbdybhyz"
user = "qbdybhyz"
password = "1cfJTjNLXvazVHYp_RhAyts0QtW_hnlo"
host = "fanny.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

# Connecting to SQLite DB

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Generic execute_query function that can work with either cursor object

def execute_query(curs, query=select_all):
    result = curs.execute(query)
    return result

def populate_pg_character_table(curs, conn, characters_list):
    for character in characters_list:
        insert_statement = '''
            INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {};
        '''.format(character[1:])
        curs.execute(insert_statement)
        conn.commit()


if __name__ == '__main__':    
    SL_CHARACTERS = execute_query(sl_curs, get_characters).fetchall()
    print(SL_CHARACTERS[:5])

    execute_query(pg_curs, create_character_table)

    populate_pg_character_table(pg_curs, pg_conn, SL_CHARACTERS)