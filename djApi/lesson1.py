import sqlite3

conn = sqlite3.connect('db.sqlite3')  # создаёт соединение с БД
cursor = conn.cursor()  # поставь курсор в SQL
SQL = '''INSERT INTO main_auto ('name', 'price', 'brand_id')
                        VALUES ('XRS', 45, 1);
'''
cursor.execute(SQL)
conn.commit()
# print(cursor.fetchall())
conn.close()

# d = dict([('ok', 100)])
# print(d)
