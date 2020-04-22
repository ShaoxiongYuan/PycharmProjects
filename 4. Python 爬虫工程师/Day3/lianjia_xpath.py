import requests
from lxml import etree
from fake_useragent import UserAgent
import pymongo


class LianjiaSpider:
    def __init__(self):
        self.url = 'https://cq.lianjia.com/ershoufang/pg{}/'
        self.headers = {
            'User-Agent': UserAgent().random
        }
        self.i = 0
        self.all_list = []
        self.conn = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.conn['housedb']
        self.myset = self.db['houseset']

    def get_data(self, url):
        for i in range(3):
            try:
                html = requests.get(url=url, headers=self.headers, timeout=3, verify=False).text
                self.parse_html(html)
                break
            except Exception as e:
                print(e)
                print('Retry')

    def parse_html(self, html):
        p = etree.HTML(html)
        li_list = p.xpath('//ul[@class="sellListContent"]/li')
        for li in li_list:
            item = {}
            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['name'] = name_list[0].strip() if name_list else None
            address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = address_list[0].strip() if address_list else None
            h_list = li.xpath('.//div[@class="houseInfo"]/text()')
            if h_list:
                info_list = h_list[0].split('|')
                if len(info_list) == 7:
                    item['model'] = info_list[0].strip()
                    item['area'] = info_list[1].strip()
                    item['direct'] = info_list[2].strip()
                    item['perfect'] = info_list[3].strip()
                    item['floor'] = info_list[4].strip()
                    item['year'] = info_list[5].strip()[:4]
                    item['type'] = info_list[6].strip()
                else:
                    item['model'] = item['area'] = item['direct'] = item['perfect'] \
                        = item['floor'] = item['year'] = item['type'] = None
            else:
                item['model'] = item['area'] = item['direct'] = item['perfect'] \
                    = item['floor'] = item['year'] = item['type'] = None
            total_list = li.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total'] = total_list[0].strip() if total_list else None
            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit'] = unit_list[0].strip() if unit_list else None
            print(item)
            self.all_list.append(item)
            self.i += 1

    def run(self):
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        for i in range(start, end + 1):
            url = self.url.format(i)
            self.get_data(url)
            print(f'第{i}页抓取成功。')
        self.myset.insert_many(self.all_list)
        print(self.i)


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
