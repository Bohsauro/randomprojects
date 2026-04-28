import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('users.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if it already exists (for clean setup)

# SQL query to create the table
table_creation_query = """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Username CHAR(25) NOT NULL,
        Password CHAR(25) NOT NULL,
        Creation_date INT NOT NULL
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

# Confirm that the table has been created
print("Table is Ready")

# Close the connection to the database
connection_obj.close()