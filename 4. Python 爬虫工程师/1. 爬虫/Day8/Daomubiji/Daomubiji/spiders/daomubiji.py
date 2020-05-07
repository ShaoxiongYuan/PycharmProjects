# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomubijiItem
import os


class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomubijiItem()
            parent_title = a.xpath('./text()').get()
            parent_url = a.xpath('./@href').get()
            item['directory'] = './novel/{}'.format(parent_title)
            if not os.path.exists(item['directory']):
                os.makedirs(item['directory'])
            yield scrapy.Request(url=parent_url, meta={'item': item},
                                 callback=self.detail_page)

    def detail_page(self, response):
        meta_1 = response.meta['item']
        art_list = response.xpath('//article')
        for art in art_list:
            item = DaomubijiItem()
            item['son_title'] = art.xpath('./a/text()').get()
            son_url = art.xpath('./a/@href').get()
            item['directory'] = meta_1['directory']

            yield scrapy.Request(url=son_url, meta={'item': item}, callback=self.get_content)

    def get_content(self, response):
        item = response.meta['item']
        content_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['content'] = '\n'.join(content_list)
        yield item
