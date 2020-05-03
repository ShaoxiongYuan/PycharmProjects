# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .settings import *


class KfcPipeline:
    def process_item(self, item, spider):
        return item


class KfcMysqlPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into kfcdb.kfctab values (%s,%s,%s,%s,%s)'
        lis = [
            item['row_num'],
            item['store_name'],
            item['address_detail'],
            item['city_name'],
            item['province_name'],
        ]
        self.cur.execute(sql, lis)
        self.db.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
