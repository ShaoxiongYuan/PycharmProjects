# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/cq/buy/o1/#bread']
    o = 1

    def parse(self, response):
        li_list = response.xpath('//ul[contains(@class,"carlist")]/li')
        for li in li_list:
            item = GuaziItem()
            item['name'] = li.xpath('./a[1]/@title').get()
            item['link'] = li.xpath('./a[1]/@href').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()

            yield item
        # 下一页URL
        if self.o < 5:
            self.o += 1
            next_url = 'https://www.guazi.com/cq/buy/o{}/#bread'.format(self.o)
            yield scrapy.Request(url=next_url, callback=self.parse)
