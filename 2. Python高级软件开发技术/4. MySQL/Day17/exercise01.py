import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='65460035', database='student', charset='utf8')

cur = db.cursor()

name = input("Name:")
score = input('Score:')

# sql = "select * from student.class_1 where name = '%s'" % name
sql = "select * from student.class_1 where name = %s or score > %s"

cur.execute(sql, [name, score])

for i in cur:
    print(i)

cur.close()
db.close()
