import psycopg2

conn = psycopg2.connect(dbname='django_pg', user='eugene',
                        password='123', host='localhost')

cursor = conn.cursor()

# SQL = """
#     CREATE TABLE less1
#     (
#         Id SERIAL PRIMARY KEY,
#         FirstName VARCHAR(30),
#         LastName VARCHAR(30),
#         Email VARCHAR(30),
#         Age INTEGER
#     )
# """

# SQL = """
#     INSERT INTO product (product_name,
#             company_name,
#             description,
#             price)
#
#         VALUES ('TT',
#             'Audi',
#             'автомобиль',
#             35000);
# """

# SQL = """
#     SELECT * FROM main_auto WHERE brand_id IN (SELECT id FROM main_brand WHERE name IN ('Audi', 'BMW'));
# """

SQL = """
    SELECT * FROM main_auto WHERE brand_id IN (SELECT id FROM main_brand WHERE name <> 'Audi'); 
"""

cursor.execute(SQL)

print(cursor.fetchall())


conn.commit()
conn.close()

