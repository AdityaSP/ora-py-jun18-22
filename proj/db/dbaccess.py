import sqlite3
conn = sqlite3.connect('users.db')
cur = conn.cursor()

# #DDL
# create_table = '''
# create table users (
# name TEXT,
# sal REAL
# )
# '''
#
# cur.execute(create_table)



# insert_data = '''
# insert into users values('Aditya',100000)
# '''
# cur.execute(insert_data)
# conn.commit()

# data = [
#     ('Arun', 2000),
#     ('Mark', 30000),
#     ('Joe', 40000)
# ]
# insert_many = '''
# insert into users values(?,?)
# '''
# cur.executemany(insert_many, data)

# select = '''
# select * from users
# '''
# cur.execute(select)
# for name,sal in cur.fetchall():
#     print name, 'earns', sal

conn.commit()
cur.close()
conn.close()