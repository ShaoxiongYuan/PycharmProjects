import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password="65460035", database='books', charset='utf8')

cur = db.cursor()

sql = "insert into index_test (name) values (%s);"
exe = []
s = "Tom"
for i in range(2000000):
    name = s + str(i)
    exe.append(name)

try:
    cur.executemany(sql, exe)
    db.commit()
except:
    db.rollback()

db.close()
