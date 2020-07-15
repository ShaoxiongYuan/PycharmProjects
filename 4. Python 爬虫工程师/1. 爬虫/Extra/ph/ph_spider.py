import requests
import re


class PHSpider:
    def __init__(self):
        self.url = 'https://www.pornhub.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
        }

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self, html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def get_data(self):
        html = self.get_html(self.url)
        pattern = r'<li class="pcVideoListItem.*?<a href="(.*?)".*?</a>'
        res = self.parse_html(html, pattern)
        for item in res:
            with open('ph.txt', 'a', encoding='utf=8') as f:
                f.write('https://www.pornhub.com' + item + '\n')
                print('https://www.pornhub.com' + item)

    def run(self):
        self.get_data()


if __name__ == '__main__':
    spider = PHSpider()
    spider.run()
