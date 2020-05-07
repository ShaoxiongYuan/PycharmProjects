import requests
from threading import Thread, Lock
import time

from fake_useragent import UserAgent
from queue import Queue


class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'
        self.q = Queue()
        self.lock = Lock()

    def url_in(self):
        for start in range(0, 692, 20):
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
                html = self.get_html(url)
                item = {}
                for one_film in html:
                    item['rank'] = one_film['rank']
                    item['name'] = one_film['title']
                    item['time'] = one_film['release_date']
                    item['score'] = one_film['score']
                    print(item)
            else:
                self.lock.release()
                break

    def run(self):
        self.url_in()
        jobs = []
        for i in range(2):
            t = Thread(target=self.parse_html)
            jobs.append(t)
            t.start()

        for job in jobs:
            job.join()


if __name__ == '__main__':
    start_time = time.time()
    spider = DoubanSpider()
    spider.run()
    end_time = time.time()
    print('time:%.2f' % (end_time - start_time))
