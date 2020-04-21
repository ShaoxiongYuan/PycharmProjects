import requests
import re
import time
import random
import pymysql


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
        }

    def get_data(self, url):
        html = requests.get(url=url, headers=self.headers).text
        res = self.parse_html(html)
        return res

    def parse_html(self, html):
        pattern = re.compile(
            r'<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            re.S)
        res = pattern.findall(html)
        return res

    def save_html(self, res):
        db = pymysql.connect(host='localhost', port=3306, user='root',
                             password='65460035', database='maoyandb', charset='utf8')

        cur = db.cursor()
        sql = "insert into maoyandb.maoyantab (name,star,time) VALUES (%s,%s,%s);"
        try:
            cur.executemany(sql, res)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

        cur.close()
        db.close()

    def run(self):
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        for i in range(start, end + 1):
            offset = (i - 1) * 10
            url = self.url.format(offset)
            res = self.get_data(url)
            res_after = []
            for item in res:
                data = (item[0].strip(), item[1].strip(), item[2].strip())
                res_after.append(data)
            self.save_html(res_after)
            time.sleep(random.randint(1, 2))
            print(f'第{i}页抓取成功。')


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
