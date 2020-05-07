import requests
from threading import Thread, Lock
import time

from fake_useragent import UserAgent
from queue import Queue
import json


class DoubanSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.q = Queue()
        self.lock = Lock()
        self.all_list = []
        self.f = open('chat_apps.json', 'w', encoding='utf-8')

    def url_in(self):
        for start in range(0, (2000 + 30) // 30):
            page_url = self.url.format(start)
            self.q.put(page_url)

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).json()
        return html

    def parse_html(self):
        while True:
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                self.lock.release()
                html = self.get_html(url)['data']
                for one_app in html:
                    item = {
                        'name': one_app['displayName'],
                        'icon': one_app['icon']
                    }
                    print(item)
                    self.lock.acquire()
                    self.all_list.append(item)
                    self.lock.release()
            else:
                self.lock.release()
                break

    def run(self):
        self.url_in()
        jobs = []
        for i in range(100):
            t = Thread(target=self.parse_html)
            jobs.append(t)
            t.start()

        for job in jobs:
            job.join()

        json.dump(self.all_list, self.f, ensure_ascii=False)


if __name__ == '__main__':
    start_time = time.time()
    spider = DoubanSpider()
    spider.run()
    end_time = time.time()
    print('time:%.2f' % (end_time - start_time))
