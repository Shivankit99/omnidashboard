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
if(len(result)!=0):
    result=result[-1]
    lid=result[0]
    print(lid)
    uid=lid+1
    print(uid)
else:
    uid=1

for d in data:
    unid=d[0]
    att=d[1] 
    rm=d[2]   
    cursor.execute(''' INSERT INTO omnidash_att (id,dadded,d1,d2,username_id,reportingmanager) VALUES (?,?,?,?,?,?)''',(uid,today,att,'Oflline',unid,rm))
    uid+=1

cursor.execute('''SELECT * from omnidash_att''')
conn.commit()
result= cursor.fetchall()
print(result)