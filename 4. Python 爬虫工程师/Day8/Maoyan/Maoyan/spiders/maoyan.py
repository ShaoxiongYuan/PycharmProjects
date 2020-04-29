# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        for i in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset={}'.format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()').get()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
            yield item
