import hashlib
import re
import sys
import requests
from lxml import etree
import redis


class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
        }
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=1)

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self, html, exp):
        p = etree.HTML(html)
        res = p.xpath(exp)
        return res

    def get_data_1(self):
        one_html = self.get_html(self.url)
        one_xpath = '//table//tr[2]/td[2]/a/@href'
        res = self.parse_html(one_html, one_xpath)
        if res:
            two_url = 'http://www.mca.gov.cn' + res[0]
            finger = self.md5_url(two_url)
            if self.r.sadd('mzb:spider', finger) == 1:
                self.get_data_2(two_url)
            else:
                sys.exit('更新完成')
        else:
            print('获取新页面链接失败')

    def get_data_2(self, url):
        two_html = self.get_html(url)
        real_url = self.get_real_url(two_html)
        real_html = self.get_html(real_url)
        two_xpath = '//tr[@height="19"]'
        tr_list = self.parse_html(real_html, two_xpath)
        for tr in tr_list:
            item = {
                'name': tr.xpath('./td[3]/text()')[0].strip(),
                'code': tr.xpath('./td[2]/text() | ./td[2]/span/text()')[0].strip()
            }
            print(item)

    def get_real_url(self, html):
        """
        获取真实返回数据的URL
        :param html:
        :return:
        """
        regex = r'window.location.href="(.*?)"'
        pattern = re.compile(regex, re.S)
        res = pattern.findall(html)
        return res[0]

    def md5_url(self, url):
        m = hashlib.md5()
        m.update(url.encode())
        return m.hexdigest()

    def run(self):
        self.get_data_1()


if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()
