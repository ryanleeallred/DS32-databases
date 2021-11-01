import sqlite3
import queries as q

# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

# Make cursor, execute query, and pull results
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results

# run the code below if this file is run as a script from the Command Line
if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    # results = execute_q(conn, q.select_few)
    print(results[:5])



# # Step 1 - Connect to the DB
# # triple-check your DB name
# connection = sqlite3.connect('rpg_db.sqlite3')

# # Step 2 - Make the "cursor"
# cursor = connection.cursor()

# # Step 3 - Write the query (in the queries.py file now!)
# # select_all = 'SELECT * FROM charactercreator_character;'

# # Step 4 - Execute the query on the cursor
# cursor.execute(q.select_all)

# # Step 5 - Pull the results from the cursor
# results = cursor.fetchall()

# print(results)
