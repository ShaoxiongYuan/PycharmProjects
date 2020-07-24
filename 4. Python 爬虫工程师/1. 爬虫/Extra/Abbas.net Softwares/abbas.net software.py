import time
import requests
import re
from fake_useragent import UserAgent


class SoftwareSpider:
    def __init__(self):
        self.url = 'https://abbaspc.net/page/{}'
        self.f = open('software.txt', 'a', encoding='utf-8')

    def get_html(self, url):
        html = requests.get(url=url, headers={
            'User-Agent': UserAgent().random
        }).text
        return html

    def parse_html(self, html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def get_data(self, url):
        html = self.get_html(url)
        pattern = r'<h3 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h3>'
        res = self.parse_html(html, pattern)
        for item in res:
            print(item[1])
            self.get_data_2(item[0], item[1])

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
        time.sleep(1)

    def run(self):
        for i in range(1, 325):
            self.get_data(self.url.format(i))
            print('*' * 50)
            print('第%d页爬取完毕。' % i)
            time.sleep(1)
        self.f.close()


if __name__ == '__main__':
    spider = SoftwareSpider()
    spider.run()
