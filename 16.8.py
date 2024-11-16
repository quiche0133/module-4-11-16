import sqlite3

connection = sqlite3.connect('books.db')

cursor = connection.cursor()

create_table_query = """
books (
    title The Weirdstone of Brisingamen,
    author Alan Garner,
    year 1960
);
"""

cursor.execute(create_table_query)

connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute("SELECT The Weirdstone of Brisingamen FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

connection.close()