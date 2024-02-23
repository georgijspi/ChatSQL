import sqlite3
import random

# Connect to the 'chinook.db' database
conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

# Create the 'rating' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rating (
        id INTEGER PRIMARY KEY,
        track_id INTEGER,
        rating_value INTEGER
    )
''')

# Generate and insert random ratings (values between 0 and 100)
for track_id in range(1, 3504):
    rating_value = random.randint(0, 100)
    cursor.execute('INSERT INTO rating (track_id, rating_value) VALUES (?, ?)', (track_id, rating_value))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table 'rating' created and populated with random values.")
