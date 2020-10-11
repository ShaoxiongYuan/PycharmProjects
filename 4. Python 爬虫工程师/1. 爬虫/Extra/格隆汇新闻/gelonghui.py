import requests
import time
import csv


class GelonghuiSpider:
    def __init__(self):
        self.url = 'https://www.gelonghui.com/api/live-channels/all/lives?onlyShowImportant=false&liveId={}&limit=15&timestamp=1589118661506'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'}
        self.f = open('detail.csv', 'w', encoding='utf-8')
        self.writer = csv.writer(self.f)
        self.all_data = []

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).json()
        return html

    def get_data(self, url):
        html = self.get_html(url)
        for detail in html['result']:
            item = (
                detail['title'].lstrip('【').strip('】'),
                detail['content'],
                time.strftime('%H:%M', time.localtime(detail['createTime']))
            )
            print(item)
            self.all_data.append(item)

    def run(self):
        for i in range(3):
            url = self.url.format(str(375582 - i * 15))
            self.get_data(url)

        self.writer.writerows(self.all_data)


if __name__ == '__main__':
    spider = GelonghuiSpider()
    spider.run()
