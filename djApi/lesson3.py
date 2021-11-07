import psycopg2

conn = psycopg2.connect(dbname='practice_db', user='eugene',
                        password='123', host='localhost')

cursor = conn.cursor()

SQL = """
    CREATE TABLE less1
    (
        Id SERIAL PRIMARY KEY,
        FirstName VARCHAR(30),
        LastName VARCHAR(30),
        Email VARCHAR(30),
        Age INTEGER
    )
"""

cursor.execute(SQL)

conn.commit()
conn.close()

