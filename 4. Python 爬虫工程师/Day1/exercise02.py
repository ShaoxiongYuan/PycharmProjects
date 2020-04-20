import random
import time

import requests
from urllib import parse


class TiebaSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
        }

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self):
        pass

    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def run(self):
        name = input('请输入贴吧名：')
        start = int(input('起始页：'))
        end = int(input('终止页：'))
        params = parse.quote(name)
        for i in range(start, end + 1):
            pn = (i - 1) * 50
            url = self.url.format(params, pn)
            html = self.get_html(url)
            filename = '{}_第{}页.html'.format(name, i)
            self.save_html(filename, html)
            time.sleep(random.uniform(1, 2))
            print(f'第{i}页抓取完成。')


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()
