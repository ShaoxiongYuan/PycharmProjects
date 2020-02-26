import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='65460035', database='dict', charset='utf8')

cur = db.cursor()

sql = "insert into dict.words (word, meaning) VALUES (%s,%s)"

values = []

with open("dict.txt") as f:
    for line in f:
        word = line.split(" ", 1)[0]
        meaning = line.lstrip(word).lstrip()
        values.append((word, meaning))

try:
    cur.executemany(sql, values)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()
