# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymongo
from .settings import *


class GuaziPipeline:
    def process_item(self, item, spider):
        print(dict(item))
        return item


class GuaziMysqlPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into cardb.cartab values (%s,%s,%s)'
        li = [
            item['name'], item['price'], item['link']
        ]
        self.cur.execute(sql, li)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()


class GuaziMongoPipeline:
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))
        return item
