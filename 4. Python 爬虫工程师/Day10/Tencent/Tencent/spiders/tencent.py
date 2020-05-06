# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import requests
import json
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn'
    keyword = input('关键字:')
    keyword = parse.quote(keyword)

    def start_requests(self):
        total = self.get_total()
        for index in range(1, total + 1):
            url = self.one_url.format(self.keyword, index)
            yield scrapy.Request(url=url, callback=self.parse_one_page)

    def get_total(self):
        url = self.one_url.format(self.keyword, 1)
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        html = requests.get(url=url, headers=headers).json()
        total = int(html['Data']['Count'])
        total = total // 10 if total % 10 == 0 else total // 10 + 1
        return total

    def parse_one_page(self, response):
        html = json.loads(response.text)
        for job in html['Data']['Posts']:
            post_id = job['PostId']
            two_url = self.two_url.format(post_id)
            yield scrapy.Request(url=two_url, callback=self.parse_two_page)

    def parse_two_page(self, response):
        html = json.loads(response.text)
        item = TencentItem()
        item['job_name'] = html['Data']['RecruitPostName']
        item['job_type'] = html['Data']['CategoryName']
        item['job_duty'] = html['Data']['Responsibility'].replace('\n', ' ').replace('\xa0', '')
        item['job_require'] = html['Data']['Requirement'].replace('\n', ' ').replace('\xa0', '')
        item['job_add'] = html['Data']['LocationName']
        item['job_time'] = html['Data']['LastUpdateTime']

        yield item
