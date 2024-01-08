import sys
import sqlite3

# Check if the user provided the database file as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python print-tables.py database.db")
    sys.exit(1)

# Get the database file path from the command line argument
db_file = sys.argv[1]

# Connect to the specified SQLite database
try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get a list of all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print the table names
    if tables:
        print("Tables in the database:")
        for table in tables:
            print(table[0])
    else:
        print("The database does not contain any tables.")

    # Close the database connection
    conn.close()

except sqlite3.Error as e:
    print("Error:", e)
    sys.exit(1)
