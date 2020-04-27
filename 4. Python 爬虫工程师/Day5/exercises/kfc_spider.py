import requests
import json
from fake_useragent import UserAgent


class KFC_Spider:
    def __init__(self):
        self.url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
        self.headers = {'User-Agent': UserAgent().random}
        self.filename = '{}.json'
        self.all_data = []

    def get_html(self, name):
        data = {
            "cname": name,
            "pid": "",
            "pageIndex": "1",
            "pageSize": "10"
        }
        html = requests.post(url=self.url, data=data, headers=self.headers).json()
        count = html['Table'][0]['rowcount']
        self.get_result(count, name)

    def get_result(self, count, name):
        for i in range(0, (count + 10) // 10):
            data = {
                "cname": name,
                "pid": "",
                "pageIndex": str(i + 1),
                "pageSize": "10"
            }
            html = requests.post(url=self.url, data=data, headers=self.headers).json()
            print(html['Table1'])
            for info in html['Table1']:
                self.all_data.append(info)

    def run(self):
        name = input('城市：')
        self.get_html(name)
        filename = self.filename.format(name)
        with open(filename, 'a', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False)


if __name__ == '__main__':
    spider = KFC_Spider()
    spider.run()
