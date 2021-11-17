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

# SQL = """
#     SELECT * FROM main_auto WHERE brand_id IN (SELECT id FROM main_brand WHERE name <> 'Audi');
# """

# SQL = """
#     SELECT * FROM main_auto WHERE price BETWEEN 5000 AND 20000;
# """

# %: соответствует любой подстроке, которая может иметь любое количество символов, при этом подстрока может и не
# содержать ни одного символа
# Например, выражение WHERE ProductName LIKE 'Galaxy%' соответствует таким значениям как "Galaxy Ace 2" или "Galaxy S7"
# _: соответствует любому одиночному символу
# Например, выражение WHERE ProductName LIKE 'Galaxy S_' соответствует таким значениям как "Galaxy S7" или "Galaxy S8".

# SQL = """
#     SELECT * FROM main_auto WHERE name LIKE 'X_';
# """

# SQL = """
#     SELECT ROUND(AVG(price), 2) AS avg_price FROM main_auto;
# """

# SQL = """
#     SELECT COUNT(*) FROM main_auto WHERE name LIKE 'X_';
# """

# Если конкретно указывать поле, то будет считать только те строки, где это поле не равно NULL.
# SQL = """
#     SELECT COUNT(DISTINCT price) FROM main_auto;
# """

# типа GROUP_CONCAT
# SQL = """
#     SELECT STRING_AGG(name, '||') FROM main_auto;
# """

# GROUP_BY
SQL = """
    SELECT name, COUNT(*) FROM main_auto GROUP BY name HAVING COUNT(*) >= 1;
"""

cursor.execute(SQL)

print(cursor.fetchall())


conn.commit()
conn.close()

