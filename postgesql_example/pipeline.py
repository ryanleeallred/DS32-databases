'''File to migrate sqlite db to postgresql'''

import psycopg2
from queries import *
import sqlite3

# Connect to Postgres DB

DBNAME = 'pmbacdky'
USER = 'pmbacdky'
PASSWORD = 'L_RjLu1KFSiclTBAEnL76CUBdPTDKFiS'
HOST = 'fanny.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

# Connect to SQLite DB

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

def execute_query_sl(curs, conn, query):
    '''User cursor to execute a given query'''
    results = curs.execute(query).fetchall()
    return results

def execute_query_pg(curs, conn, query):
    '''User cursor to execute a given query'''
    results = curs.execute(query)
    conn.commit()
    return results

if __name__ == '__main__':
    # execute_query(pg_curs, pg_conn, create_table)
    # execute_query(pg_curs, pg_conn, insert_data)
    # execute_query(pg_curs, pg_conn, select_all)

    # look at the schema of the table
    # print(execute_query(sl_curs, sl_conn, get_character_table))

    # Get characters from SQLite
    character_list = execute_query_sl(sl_curs, sl_conn, get_characters)
    # print(characters_list)

    # Make the Postgres DB table
    execute_query_pg(pg_curs, pg_conn, create_character_table)

    # Take Character data and insert into Postgres DB
    # loop over the characters
    # grab all values from the character tuple EXCEPT for character_id
    for character in character_list:
        insert_statement = '''
            INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {};
            '''.format(character[1:])
        execute_query_pg(pg_curs, pg_conn, insert_statement)






    
