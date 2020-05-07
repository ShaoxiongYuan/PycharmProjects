# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['www.guazi.com']

    def start_requests(self):
        """
        所有URL交给scheduler
        :return:
        """
        for o in range(1, 6):
            url = 'https://www.guazi.com/cq/buy/o{}/#bread'.format(o)
            yield scrapy.Request(url=url, callback=self.parse_one_page)

    def parse_one_page(self, response):
        li_list = response.xpath('//ul[contains(@class,"carlist")]/li')
        for li in li_list:
            item = GuaziItem()
            item['name'] = li.xpath('./a[1]/@title').get()
            item['link'] = li.xpath('./a[1]/@href').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()

            yield item
