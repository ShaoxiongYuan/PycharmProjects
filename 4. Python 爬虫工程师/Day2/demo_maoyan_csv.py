import csv
import requests
import re
import time
import random


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
        }
        self.f = open('maoyan.csv', 'a', newline='')
        self.writer = csv.writer(self.f)
        self.all_list = []

    def get_data(self, url):
        html = requests.get(url=url, headers=self.headers).text
        res = self.parse_html(html)
        return res

    def parse_html(self, html):
        pattern = re.compile(
            r'<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            re.S)
        res = pattern.findall(html)
        return res

    def save_html(self, res):
        for item in res:
            data = (item[0].strip(), item[1].strip(), item[2].strip())
            self.all_list.append(data)

    def run(self):
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        for i in range(start, end + 1):
            offset = (i - 1) * 10
            url = self.url.format(offset)
            res = self.get_data(url)
            self.save_html(res)
            # time.sleep(random.randint(1, 2))
            print(f'第{i}页抓取成功。')
        self.writer.writerows(self.all_list)
        self.f.close()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
