import os
import requests
import re
import random
import time
from fake_useragent import UserAgent
from urllib import parse


class BaiduPicSpider:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.name = input('需要查询的内容：')
        self.directory = './pictures/{}/'.format(self.name)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.i = 1

    def get_html(self, url):
        html = requests.get(url=url, headers={'User-Agent': UserAgent().random})
        return html

    def parse_html(self, html):
        regex = r'"thumbURL":"(.*?)"'
        pattern = re.compile(regex, re.S)
        res = pattern.findall(html)
        return res

    def get_data(self, url):
        html = self.get_html(url).text
        res = self.parse_html(html)
        for item in res:
            html = self.get_html(item).content
            self.save_data(html)
            # time.sleep(random.randint(1, 2))

    def save_data(self, html):
        filename = '{}_第{}张图.jpg'.format(self.name, self.i)
        with open(self.directory + filename, 'wb') as f:
            f.write(html)
        self.i += 1
        print(filename + '下载成功')

    def run(self):
        url = self.url.format(parse.quote(self.name))
        self.get_data(url)


if __name__ == '__main__':
    spider = BaiduPicSpider()
    spider.run()
