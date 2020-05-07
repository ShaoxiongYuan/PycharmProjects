import json
from queue import Queue
import redis
import requests
from threading import Thread, Lock
import time
from urllib import parse
from fake_useragent import UserAgent
import hashlib


class TencentSpider:
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=us'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1587811336646&postId={}&language=zh-cn'
        self.lock_1 = Lock()
        self.lock_2 = Lock()
        self.q1 = Queue()
        self.q2 = Queue()
        self.all_data = []
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def url_in(self):
        job = input('请输入职位：')
        job = parse.quote(job)
        total = self.get_total(job)
        for i in range(1, total + 1):
            url = self.one_url.format(job, i)
            self.q1.put(url)
        return job

    def get_total(self, kw):
        url = self.one_url.format(kw, 1)
        html = self.get_html(url)
        total = int(html['Data']['Count'])
        total = total // 10 if total % 10 == 0 else total // 10 + 1
        return total

    def md5_url(self, url):
        m = hashlib.md5()
        m.update(url.encode())
        return m.hexdigest()

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).json()
        return html

    def parse_one_page(self):
        while True:
            self.lock_1.acquire()
            if not self.q1.empty():
                one_url = self.q1.get()
                self.lock_1.release()
                html = self.get_html(one_url)
                for job in html['Data']['Posts']:
                    post_id = job['PostId']
                    two_url = self.two_url.format(post_id)
                    self.lock_1.acquire()
                    self.q2.put(two_url)
                    self.lock_1.release()
            else:
                self.lock_1.release()
                break

    def parse_two_page(self):
        while True:
            try:

                url = self.q2.get(block=True, timeout=3)
            except Exception as e:
                print(e)
                break
            else:
                finger = self.md5_url(url)
                if self.r.sadd('job:spider', finger) == 1:
                    html = self.get_html(url)
                    item = {
                        'name': html['Data']['RecruitPostName'],
                        'address': html['Data']['LocationName'],
                        'type': html['Data']['CategoryName'],
                        'time': html['Data']['LastUpdateTime'],
                        'duty': html['Data']['Responsibility'].replace('\n', ' ').replace('\r', '').replace('\t', ''),
                        'requirement': html['Data']['Requirement'].replace('\n', ' ').replace('\r', '').replace('\t',
                                                                                                                '')
                    }
                    print(item)
                    self.lock_2.acquire()
                    self.all_data.append(item)
                    self.lock_2.release()
                else:
                    pass

    def run(self):
        keyword = self.url_in()

        job_1 = []
        job_2 = []
        for i in range(10):
            t = Thread(target=self.parse_one_page)
            job_1.append(t)
            t.start()

        for i in range(10):
            t = Thread(target=self.parse_two_page)
            job_2.append(t)
            t.start()

        for job in job_1:
            job.join()

        for job in job_2:
            job.join()

        with open('{}.json'.format(keyword + '职位信息'), 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False)


if __name__ == '__main__':
    start_time = time.time()
    spider = TencentSpider()
    spider.run()
    end_time = time.time()
    print('执行时间:%.2f' % (end_time - start_time))
