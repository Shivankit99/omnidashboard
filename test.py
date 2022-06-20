import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor=conn.cursor()
cursor.execute(''' UPDATE omnidash_rem SET reject=0  ''')
conn.commit()
# result= cursor.fetchall()
# for res in result:
#     for r in res:
#         print(r,type(r))