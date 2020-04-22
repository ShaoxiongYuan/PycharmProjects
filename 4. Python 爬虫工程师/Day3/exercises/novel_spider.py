import requests
import re
from fake_useragent import UserAgent


class NovelSpider:
    def __init__(self):
        self.url = 'http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html'

    @staticmethod
    def get_html(url):
        html = requests.get(url=url, headers={'User-Agent': UserAgent().random}).text
        return html

    @staticmethod
    def parse_html(html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def get_data_1(self, url):
        html = self.get_html(url)
        regex = r'<div class="bookname">.*?href="(.*?)" target=.*?>'
        res = self.parse_html(html, regex)
        for item in res:
            self.get_data_2(item)

    def get_data_2(self, url):
        html = self.get_html(url)
        regex2 = r'<a class="all-catalog".*?href="(.*?)" data-sa-d=.*?</a>'
        res = self.parse_html(html, regex2)
        if res:
            for item in res:
                self.get_data_3(item)

    def get_data_3(self, url):
        html = self.get_html(url)
        regex3 = r'<li class=" col-4">.*?href="(.*?)" target="_blank".*?</a>'
        res = self.parse_html(html, regex3)
        if res:
            for item in res:
                self.get_data_4(item)

    def get_data_4(self, url):
        html = self.get_html(url)
        regex4 = r'<title>(.*?)</title>.*?<div class="content" itemprop="acticleBody">(.*?)</div>'
        res = self.parse_html(html, regex4)
        if res:
            NovelSpider.save_data(res)

    @staticmethod
    def save_data(res):
        for item in res:
            title = item[0].split('_')[0].strip()
            chapter = item[0].split('_')[1].strip()
            filename = NovelSpider.get_filename(title, chapter)
            data = item[1].replace('<p>', '').replace('</p>', '\n').strip()
            print(data)
            with open(filename, 'w') as f:
                f.write(data)

    @staticmethod
    def get_filename(title, chapter):
        return '{}_{}.txt'.format(title, chapter) \
            .replace('?', '') \
            .replace('/', '') \
            .replace('\\', '') \
            .replace(':', '') \
            .replace('*', '') \
            .replace('"', '') \
            .replace('<', '') \
            .replace('>', '') \
            .replace('|', '')

    def run(self):
        start = int(input('请输入开始：'))
        end = int(input('请输入结束：'))
        for i in range(start, end + 1):
            url = self.url.format(i)
            self.get_data_1(url)
            print(f'第{i}页爬取完成')


if __name__ == '__main__':
    spider = NovelSpider()
    spider.run()
