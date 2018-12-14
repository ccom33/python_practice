import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")
table = cursor.fetchall()
for record in table:
    print("이름 : %s, 전화 : %s, 주소 ; %s" % record)

cursor.close()
con.close()
#------------------------------------------------------
con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr ORDER BY addr DESC")
while True:
    record = cursor.fetchone()
    if record == None:
        break
    print("이름 : %s, 전화 : %s, 주소 : %s" % record)

cursor.close()
con.close()

#-------------------------------------------------------
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT phone FROM tblAddr WHERE name = '김상형'")
record = cursor.fetchone()
print("김상형의 전화 번호는 %s 입니다." % record)

cursor.close()
con.close()
