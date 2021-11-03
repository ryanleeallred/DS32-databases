import sqlite3
import pymongo

PASSWORD = 'r7anfTcQdiTo9qKv'
DBNAME = 'test'
USERNAME = 'test-user'

# Connect to SQLite
def create_sl_conn(source_db='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(source_db)
    return sl_conn

# Query SQLiet
def execute_query(curs, query):
    return curs.execute(query).fetchall()

# Open Connection to Mongo
def create_mdb_conn(password, dbname, username, collection_name):
    client = pymongo.MongoClient('mongodb+srv://{}:{}@cluster0.9tgsq.mongodb.net/{}?retryWrites=true&w=majority'.format(username, password, dbname))
    # database that we want to connect to
    db = client[DBNAME]
    # create the collection that we want to connect to if it doesn't already exist
    col = db[collection_name]
    return col

# Create a document and insert into our collection
def char_doc_creation(collection, character_list):
    for char in character_list:
        character_doc = {
            'name': char[1],
            'level': char[2], 
            'exp': char[3], 
            'hp': char[4], 
            'strength': char[5], 
            'intelligence': char[6], 
            'dexterity': char[7], 
            'wisdom': char[8]
        }
        collection.insert_one(character_doc)

# code that will only run when executed as a script
if __name__ == '__main__':
    # Get a SQLite Cursor to use in querying the DB.
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()

    # Write query to get charactercreator_charater table
    get_characters = '''
        SELECT * FROM charactercreator_character
    '''
    # Execute the Query
    characters = execute_query(sl_curs, get_characters)

    # Save the first two characters to a list.
    # two_characters = characters[:2]

    # Open our MongoDB Connection
    col = create_mdb_conn(PASSWORD, DBNAME, USERNAME, 'characters')

    # Add a chacter to the "characters" collection
    char_doc_creation(col, characters)




