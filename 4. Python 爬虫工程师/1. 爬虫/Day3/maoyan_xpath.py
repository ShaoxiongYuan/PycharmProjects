from lxml import etree
import requests
import time
import random


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
        }

    def get_data(self, url):
        html = requests.get(url=url, headers=self.headers).text
        res = self.parse_html(html)
        return res

    def parse_html(self, html):
        p = etree.HTML(html)
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item = {'name': dd.xpath('.//p[@class="name"]/a/@title')[0].strip(),
                    'star': dd.xpath('.//p[@class="star"]/text()')[0].strip(),
                    'time': dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
                    }
            print(item)

    def run(self):
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        for i in range(start, end + 1):
            offset = (i - 1) * 10
            url = self.url.format(offset)
            res = self.get_data(url)
            # time.sleep(random.randint(1, 2))
            print(f'第{i}页抓取成功。')


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
