import sqlite3
from datetime import date

today = date.today()

#conn = sqlite3.connect('/home/pi/SOIScripts/omnidash/db.sqlite3')
conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()
cursor.execute('''SELECT * from omnidash_employee''')
conn.commit()
result= cursor.fetchall()
data = []
for i in result:    
    data.append([i[0],i[-1],i[2]])

cursor.execute('''SELECT * from omnidash_att''')
conn.commit()
result= cursor.fetchall()
   
for d in data:
    unid=d[0]
    att=d[1] 
    rm=d[2]   
    cursor.execute(''' UPDATE omnidash_att set d2 = ? WHERE username_id = ? AND dadded = ?''',(att,unid,today))

cursor.execute('''SELECT * from omnidash_att''')
conn.commit()
result= cursor.fetchall()
print(result)