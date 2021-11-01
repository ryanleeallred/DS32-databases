import sqlite3
import pandas as pd

# Step 1 - Connect to the DB
# triple-check your DB name
connection = sqlite3.connect('rpg_db.sqlite3')

# Step 2 - Make the "cursor"
cursor = connection.cursor()

# Step 3 - Write the query
query = 'SELECT * FROM charactercreator_character;'

# get table column header information
# query2 = "PRAGMA table_info('charactercreator_character');"

# Step 4 - Execute the query on the cursor
cursor.execute(query)

# Step 5 - Pull the results from the cursor
results = cursor.fetchall()

df = pd.DataFrame(data=results)

df.to_csv('characters.csv')

print(df)
