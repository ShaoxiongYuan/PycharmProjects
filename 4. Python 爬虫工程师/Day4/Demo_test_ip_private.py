"""
1. 获取代理
2. 依次测试
"""
import requests


class ProxyPool:
    def __init__(self):
        self.url = 'http://dps.kdlapi.com/api/getdps/?orderid=998769662367682&num=10&pt=1&sep=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
        }
        self.f = open('proxy.txt', 'a')

    def get_html(self):
        html = requests.get(url=self.url, headers=self.headers).text
        proxy_list = html.split('\r\n')
        for proxy in proxy_list:
            if self.check_proxy(proxy):
                self.f.write(proxy + '\n')

    def check_proxy(self, proxy):
        test_url = 'https://httpbin.org/get'
        proxies = {
            'http': 'http://749904167:fqnyelwf@{}'.format(proxy),
            'https': 'https://749904167:fqnyelwf@{}'.format(proxy)
        }
        try:
            res = requests.get(url=test_url, proxies=proxies, headers=self.headers, timeout=2)
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
        self.get_html()
        self.f.close()


if __name__ == '__main__':
    while True:
        spider = ProxyPool()
        spider.run()
