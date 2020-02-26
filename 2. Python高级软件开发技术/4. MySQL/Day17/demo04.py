import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='65460035', database='student', charset='utf8')

cur = db.cursor()

sql = 'select name,score from student.class_1 where score>75'
cur.execute(sql)

# 获取方法一
# for i in cur:
#     print(i)

# 获取方法二
print(cur.fetchone())

print(cur.fetchmany(2))

print(cur.fetchall())

cur.close()
db.close()
