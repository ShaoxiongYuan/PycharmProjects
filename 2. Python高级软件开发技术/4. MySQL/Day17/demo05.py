import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='65460035', database='student', charset='utf8')

cur = db.cursor()

values = [("Leonard", 28, 'm', 100),
          ("Harden", 32, 'm', 96),
          ("Luka", 23, 'm', 89),
          ("Kobe", 42, 'm', 99)]
# try:
#     # 1.
#     # sql = "insert into student.class_1 values (6,'Anthony',17,'m',89)"
#     # cur.execute(sql)
#
#     # 2.
#     sql = "update student.class_1 set score=%s where name=%s"
#     cur.execute(sql, [85, "Tony"])
#     db.commit()
# except:
#     db.rollback()

sql = "insert into student.class_1 (name, age, sex, score) VALUES (%s,%s,%s,%s)"
try:
    cur.executemany(sql, values)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()
