import requests
import re
from fake_useragent import UserAgent


class IPTest:
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/{}'
        self.f = open('free_ip.txt', 'w')

    @staticmethod
    def get_html(url):
        html = requests.get(url=url, headers={'User-Agent': UserAgent().random}).text
        return html

    @staticmethod
    def parse_html(html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def get_data(self, url):
        html = self.get_html(url)
        regex = r'<tr class=".*?<td class=".*?</td.*?td>(.*?)</td.*?td>(.*?)</td>'
        res = self.parse_html(html, regex)
        for item in res:
            proxy = '%s:%s' % (item[0], item[1])
            if self.check_proxy(proxy):
                self.f.write(proxy + '\n')

    def check_proxy(self, proxy):
        test_url = 'https://httpbin.org/get'
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy)
        }
        try:
            res = requests.get(url=test_url, proxies=proxies, headers={'User-Agent': UserAgent().random}, timeout=2)
            if res.status_code == 200:
                print(proxy, '\033[031m可用\033[0m')
                return True
            else:
                print(proxy, '无效')
                return False
        except Exception as e:
            print(proxy, '无效')
            return False

    def run(self):
        start = int(input('起始页：'))
        end = int(input('终止页：'))
        for i in range(start, end + 1):
            url = self.url.format(i)
            self.get_data(url)


if __name__ == '__main__':
    spider = IPTest()
    spider.run()
