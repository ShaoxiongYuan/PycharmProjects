"""
数据处理
"""
import pymysql


class Database:
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.user = 'root'
        self.password = '65460035'
        self.database = 'dict'
        self.charset = 'utf8'
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset=self.charset)

    def create_cursor(self):
        self.cur = self.db.cursor()

    def register(self, name, password):
        sql = "select name from dict.user where name=%s"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()
        if r:
            return False
        else:
            try:
                sql = "insert into dict.user (name,password) values (%s,%s)"
                self.cur.execute(sql, [name, password])
                self.db.commit()
                return True
            except:
                self.db.rollback()
                return False

    def login(self, name, password):
        sql = "select name,password from dict.user where name=%s and password=%s"
        self.cur.execute(sql, [name, password])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    def search(self, name, word):
        sql = "select meaning from dict.words where word=%s"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        if r:
            self.insert_into_history(name, word)
            return r[0]
        else:
            self.insert_into_history(name, word)
            return None

    def history(self, name):
        sql = "select name,word,time from dict.history where name=%s"
        self.cur.execute(sql, [name])
        r = self.cur.fetchmany(10)
        return r

    def insert_into_history(self, name, word):
        sql = "insert into dict.history (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
