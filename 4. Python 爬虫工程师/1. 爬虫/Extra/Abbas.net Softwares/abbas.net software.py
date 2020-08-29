import time
import requests
import re
from fake_useragent import UserAgent
import random
from hashlib import md5
import redis
import sys


class SoftwareSpider:
    def __init__(self):
        self.url = 'https://abbaspc.net/page/{}'
        self.f = open('software.txt', 'a', encoding='utf-8')
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    def get_html(self, url):
        html = requests.get(url=url, headers={
            'User-Agent': UserAgent().random
        }).text
        return html

    def parse_html(self, html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def md5_url(self, url):
        """
        对URL进行加密
        :param url:
        :return: 加密后字符串
        """
        s = md5()
        s.update(url.encode())
        return s.hexdigest()

    def get_data(self, url):
        html = self.get_html(url)
        pattern = r'<h3 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h3>'
        res = self.parse_html(html, pattern)
        for item in res:
            print(item[1])
            if item[0] != 'https://abbaspc.net/idm-crack/':
                finger = self.md5_url(item[0])
                if self.r.sadd('software:spider', finger) == 1:
                    try:
                        self.get_data_2(item[0], item[1])
                        time.sleep(random.uniform(1, 2))
                    except Exception as e:
                        self.r.srem('software:spider', finger)
                else:
                    sys.exit('更新完成')

    def get_data_2(self, url, item):
        html = self.get_html(url)
        try:
            pattern = r'<p><strong><a.*?href="(.*?)" target="_blank".*?</a></strong>'
            res = self.parse_html(html, pattern)
            self.f.write(item + '\nDownload Link: ' + res[0] + '\n' + '*' * 50 + '\n')
        except IndexError:
            try:
                pattern = r'<p><a.*?href="(.*?)" target="_blank".*?</strong></a>'
                res = self.parse_html(html, pattern)
                self.f.write(item + '\nDownload Link: ' + res[0] + '\n' + '*' * 50 + '\n')
            except IndexError:
                pass
        time.sleep(random.randint(0, 1))

    def run(self):
        for i in range(1, 327):
            self.get_data(self.url.format(i))
            print('第%d页爬取完毕。' % i)
            print('*' * 50)
            time.sleep(random.randint(1, 2))
        self.f.close()


if __name__ == '__main__':
    spider = SoftwareSpider()
    spider.run()
