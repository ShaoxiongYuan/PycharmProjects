"""
Redis集合增量爬虫
"""

import re
import requests
import time
import random
from fake_useragent import UserAgent
import pymongo
import redis
from hashlib import md5
import sys


class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        self.conn = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.conn['cardb']
        self.myset = self.db['carset']
        self.all_list = []
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    def get_html(self, url):
        agent = UserAgent().random
        html = requests.get(url=url, headers={'User-Agent': agent}).text
        return html

    def parse_html(self, html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def get_data(self, url):
        html = self.get_html(url)
        regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        res = self.parse_html(html, regex)
        for item in res:
            two_url = 'https://www.che168.com' + item
            finger = self.md5_url(two_url)
            if self.r.sadd('car:spider', finger) == 1:
                try:
                    self.get_info(two_url)
                    time.sleep(random.uniform(1, 2))
                except Exception as e:
                    self.r.srem('car:spider', finger)
            else:
                sys.exit('更新完成')

    def get_info(self, two_url):
        html = self.get_html(two_url)
        regex2 = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b'
        res = self.parse_html(html, regex2)
        self.save_data(res)
        # item = {'name': res[0][0].strip(),
        #         'mileage': res[0][1].strip(),
        #         'time': res[0][2].strip(),
        #         'type': res[0][3].split('/')[0].strip(),
        #         'displacement': res[0][3].split('/')[1].strip(),
        #         'location': res[0][4].strip(),
        #         'price': res[0][5].strip() + '万'
        #         }
        # print(item)

    def save_data(self, res):
        item = {'name': res[0][0].strip(),
                'mileage': res[0][1].strip(),
                'time': res[0][2].strip(),
                'type': res[0][3].split('/')[0].strip(),
                'displacement': res[0][3].split('/')[1].strip(),
                'location': res[0][4].strip(),
                'price': res[0][5].strip() + '万'
                }
        self.all_list.append(item)

    def md5_url(self, url):
        """
        对URL进行加密
        :param url:
        :return: 加密后字符串
        """
        s = md5()
        s.update(url.encode())
        return s.hexdigest()

    def run(self):
        start = int(input('起始页：'))
        end = int(input('终止页：'))
        for i in range(start, end + 1):
            url = self.url.format(i)
            self.get_data(url)
            print(f'第{i}页爬取成功')
        self.myset.insert_many(self.all_list)


if __name__ == '__main__':
    spider = CarSpider()
    spider.run()
