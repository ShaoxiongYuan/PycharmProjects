import sys
import pymongo
import requests
import re
import time
import random
import hashlib
import redis
from fake_useragent import UserAgent


class MovieSpider:
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/china/list_4_{}.html'
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        self.conn = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.conn['moviedb']
        self.myset = self.db['movieset']
        self.all_list = []

    def get_html(self, url):
        html = requests.get(url=url, headers={'User-Agent': UserAgent().random}).content.decode('gb2312', 'ignore')
        return html

    def parse_html(self, html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def md5_url(self, url):
        m = hashlib.md5()
        m.update(url.encode())
        return m.hexdigest()

    def get_data(self, url):
        html = self.get_html(url)
        regex = r'<td height="26">.*?</a.*?href="(.*?)" class="ulink">'
        res = self.parse_html(html, regex)
        for item in res:
            two_url = 'https://www.dytt8.net/' + item
            finger = self.md5_url(two_url)
            if self.r.sadd('movie:spider', finger) == 1:
                try:
                    self.get_info(two_url)
                    time.sleep(random.randint(1, 2))
                except Exception as e:
                    print(e)
                    self.r.srem('movie:spider', finger)
            else:
                sys.exit('更新完成')

    def get_info(self, two_url):
        html = self.get_html(two_url)
        regex2 = r'<font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP: break-word".*?<a href="(.*?)">'
        res = self.parse_html(html, regex2)
        if res:
            item = {'name': res[0][0].strip(), 'download_url': res[0][1].strip()}
            print(item)
            # self.save_data(res)

    def save_data(self, res):
        item = {'name': res[0][0].strip(), 'download_url': res[0][1].strip()}
        self.all_list.append(item)

    def run(self):
        start = int(input('起始页：'))
        end = int(input('终止页：'))
        for i in range(start, end + 1):
            url = self.url.format(i)
            self.get_data(url)
            print(f'第{i}页爬取完成')
        # self.myset.insert_many(self.all_list)


if __name__ == '__main__':
    spider = MovieSpider()
    spider.run()
