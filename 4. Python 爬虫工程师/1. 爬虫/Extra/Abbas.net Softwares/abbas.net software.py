import requests
import re


class SoftwareSpider:
    def __init__(self):
        self.url = 'https://abbaspc.net/page/{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0'
        }

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self, html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def get_data(self, url):
        html = self.get_html(url)
        pattern = r'<a href="(.*?)" rel="bookmark">(.*?)</a></h3>'
        res = self.parse_html(html, pattern)
        for item in res:
            with open('software.txt', 'a', encoding='utf=8') as f:
                f.write(item[1] + '\n')
                print(item[1])

    def run(self):
        for i in range(1, 324):
            self.get_data(self.url.format(i))
            print('*' * 50)
            print('第%d页爬取完毕。' % i)


if __name__ == '__main__':
    spider = SoftwareSpider()
    spider.run()
