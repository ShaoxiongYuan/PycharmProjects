# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'

    def start_requests(self):
        for sn in range(0, 121, 30):
            url = self.url.format(sn)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        html = json.loads(response.text)
        for pic in html['list']:
            item = SoItem()
            item['img_title'] = pic['title'].strip('?')
            item['img_url'] = pic['qhimg_url']
            yield item
