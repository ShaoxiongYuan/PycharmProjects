import requests
from fake_useragent import UserAgent
import time
import random
import re
import json


class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0
        # 存入json文件
        self.f = open('douban.json', 'w', encoding='utf-8')
        self.all_film_list = []

    def get_agent(self):
        return UserAgent().random

    def get_html(self, params):
        headers = {'User-Agent': self.get_agent()}
        html = requests.get(url=self.url, params=params, headers=headers).text
        # 把json格式的字符串转为python数据类型
        html = json.loads(html)
        self.parse_html(html)

    def parse_html(self, html):
        """解析"""
        # html: [{},{},{},{}]
        item = {}
        for one_film in html:
            item['rank'] = one_film['rank']
            item['title'] = one_film['title']
            item['score'] = one_film['score']
            print(item)
            self.all_film_list.append(item)
            self.i += 1

    def run(self):
        # d: {'剧情':'11','爱情':'13','喜剧':'5',...,...}
        d = self.get_d()
        # 1、给用户提示,让用户选择
        menu = ''
        for key in d:
            menu += key + '|'
        print(menu)
        choice = input('请输入电影类别：')
        if choice in d:
            code = d[choice]
            # 2、total: 电影总数
            total = self.get_total(code)
            for start in range(0, total, 20):
                params = {
                    'type': code,
                    'interval_id': '100:90',
                    'action': '',
                    'start': str(start),
                    'limit': '20'
                }
                self.get_html(params=params)
                time.sleep(random.randint(1, 2))

            # 把数据存入json文件
            json.dump(self.all_film_list, self.f, ensure_ascii=False)
            self.f.close()
            print('数量:', self.i)
        else:
            print('请做出正确的选择')

    def get_d(self):
        """{'剧情':'11','爱情':'13','喜剧':'5',...,...}"""
        url = 'https://movie.douban.com/chart'
        html = requests.get(url=url, headers={'User-Agent': self.get_agent()}).text
        regex = '<span><a href=".*?type_name=(.*?)&type=(.*?)&interval_id=100:90&action=">'
        pattern = re.compile(regex, re.S)
        # r_list: [('剧情','11'),('喜剧','5'),('爱情':'13')... ...]
        r_list = pattern.findall(html)
        # d: {'剧情': '11', '爱情': '13', '喜剧': '5', ..., ...}
        d = {}
        for r in r_list:
            d[r[0]] = r[1]
        return d

    def get_total(self, code):
        """获取某个类别下的电影总数"""
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(code)
        html = requests.get(url=url, headers={'User-Agent': self.get_agent()}).text
        html = json.loads(html)
        return html['total']


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
