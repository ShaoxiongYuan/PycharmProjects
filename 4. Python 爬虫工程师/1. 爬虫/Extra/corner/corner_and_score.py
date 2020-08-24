"""
https://www.dszuqiu.com/league/35/p.1?type=ended_race
"""
import re
from fake_useragent import UserAgent
import requests
from lxml import etree
import time
import random
import csv


class CornerAndScore:
    def __init__(self):
        self.url = "https://www.dszuqiu.com/league/35/p.{}?type=ended_race"
        self.list = []
        self.count = 0

    def get_html(self):
        total = self.get_total()
        print(total)
        for i in range(1, total):
            html = requests.get(url=self.url.format(i), headers={'User-Agent': UserAgent().random}).text
            self.xpath_func(html)

    def xpath_func(self, html):
        p = etree.HTML(html)
        r_list = p.xpath('//*[@id="ended"]/table//tr')
        self.parse_html(r_list)

    def parse_html(self, r_list):
        self.count += 1
        for one_match_corner in r_list[1:]:
            # one_match_corner_list = []
            red_team = one_match_corner.xpath('.//td[@class="text-right BR0"]/a/text()')[0].strip()
            blue_team = one_match_corner.xpath('.//td[@class="text-left"]/a/text()')[0].strip()
            match_date = one_match_corner.xpath('.//td[3]/text()')[0].strip()
            one_match_total_list = [red_team, blue_team, match_date]
            value = one_match_corner.xpath('.//span[@class="timeLineCorner"]/@title')
            for i in value:
                list_corner_min = i.split(' - ')
                one_match_total_list.append(tuple(list_corner_min))
                # one_math_total_list.append(tuple('\n'))
            self.list.append(tuple(one_match_total_list))
            time.sleep(random.uniform(1, 2))
        print('第{}页完成'.format(self.count))

    def get_total(self):
        html = requests.get(url=self.url.format(1), headers={'User-Agent': UserAgent().random}).text
        regex = r'.*?radius">...</a>.*?ended_race">(.*?)</a>'
        pattern = re.compile(regex, re.S)
        total = int(pattern.findall(html)[0])
        print(total)
        return total

    def save_corner_score(self):
        with open('角球数据汇总.csv', 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(self.list)

    def run(self):
        self.get_html()
        self.save_corner_score()


if __name__ == '__main__':
    spider = CornerAndScore()
    spider.run()

"""
.*?ended_race">(.*?)</a>.*?<select

.*?radius">...</a>.*?ended_race">(.*?)</a>
"""
