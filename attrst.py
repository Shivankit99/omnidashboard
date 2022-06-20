import sqlite3

#conn = sqlite3.connect('/home/pi/SOIScripts/omnidash/db.sqlite3')
conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()
# cursor.execute('''SELECT * from omnidash_employee''')
# conn.commit()
# result= cursor.fetchall()
# print(result)
cursor.execute(''' UPDATE omnidash_employee SET status = 'Offline' ''') 
cursor.execute('''SELECT * from omnidash_employee''')
conn.commit()
result= cursor.fetchall()
print(result)

