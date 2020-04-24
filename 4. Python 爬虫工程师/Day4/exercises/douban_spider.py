import pymongo
import requests
import re


class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/chart'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
        }
        self.url_2 = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        self.url_count = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'
        self.conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.conn['doubanmovie_db']
        self.all_list = []

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers)
        return html

    def parse_html(self, html, pattern):
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        return res

    def get_movie_type(self):
        html = self.get_html(self.url).text
        regex = r'<span><a href=".*?">(.*?)</a></span>'
        return self.parse_html(html, regex)

    def get_data(self, num):
        html = self.get_html(self.url).text
        regex = r'<span><a href="(.*?)">(.*?)</a></span>'
        res = self.parse_html(html, regex)
        if num == 30:
            for item in res:
                type = item[0].split('&')[1][5:]
                self.get_data_2(type)
                myset = self.db[item[1]]
                myset.insert_many(self.all_list)
                self.all_list = []
        else:
            self.get_data_2(res[num - 1][0].split('&')[1][5:])

    def get_data_2(self, type):
        url = self.url_count.format(type)
        html = self.get_html(url).json()
        total = html['total']
        for i in range(0, total, 20):
            url = self.url_2.format(type, i)
            html = self.get_html(url).json()
            for film in html:
                self.save_data(film)

    def save_data(self, film):
        item = {
            'name': film['title'],
            'score': film['score'],
            'rank': film['rank'],
            'releaseDate': film['release_date']
        }
        type = ''
        for one_type in film['types']:
            type += one_type + '、'
        item['types'] = type.strip('、')
        actor = ''
        for one_actor in film['actors']:
            actor += one_actor + '、'
        item['actors'] = actor.strip('、')
        print(item)
        self.all_list.append(item)

    def run(self):
        res = self.get_movie_type()
        data = []
        for index, type in enumerate(res):
            data.append({index + 1: type})
            print({index + 1: type})
        print('请输入电影类型对应编号，全部搜索请输30')
        choice = int(input('请输入编号：'))
        if choice == 30:
            self.get_data(choice)
        else:
            for item in data:
                if choice in item.keys():
                    self.get_data(choice)
                    myset = self.db['%s' % item[choice]]
                    myset.insert_many(self.all_list)


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
