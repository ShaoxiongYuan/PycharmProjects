import requests
import re
from lxml import etree


class CaijingSpider:
    def __init__(self):
        self.url = 'http://finance.ce.cn/rolling/index.shtml'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'}

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).content.decode('gb2312', 'ignore')
        return html

    def parse_html(self, html, regex):
        p = etree.HTML(html)

        pattern = re.compile(regex, re.S)
        result = pattern.findall(html)
        return result

    def get_data(self):
        html = self.get_html(self.url)
        pattern = r'<tr>.*?td height="28".*?<a href="(.*?)" target=.*?</tr>'
        res = self.parse_html(html, pattern)
        for url in res:
            if url[0] == 'h':
                self.get_data_2(url)
            elif url[0] == '.' and url[1] == '.':
                self.get_data_2('http://finance.ce.cn' + url[2:])
            else:
                self.get_data_2('http://finance.ce.cn/rolling' + url[1:])

    def get_data_2(self, url):
        html = self.get_html(url)
        pattern = r'<div class=TRS_Editor>(.*)。.*?责任编辑：'
        # pattern = r'<div class="neirong".*?Title">(.*?)</h1>.*?id="articleTime">(.*?)</span>.*?id="articleSource">(.*?)</span>.*?<div class=TRS_Editor>(.*?)<strong>'
        res = self.parse_html(html, pattern)
        for item in res:
            result = re.sub('[0-9a-zA-Z]', ' ', item, re.S)
            # result = re.sub('\s+', ' ', result, re.S)
            print(result)
            print('**************************************')
            # print(item[1].strip().strip('\n'))
            # print(item[2].strip().strip('\n'))
            # print(item[3].strip().replace('<p>', '').replace('</p>', '\n'))

    def run(self):
        self.get_data()


if __name__ == '__main__':
    spider = CaijingSpider()
    spider.run()

html = """<div class=TRS_Editor>(.*)。.*?责任编辑："""
