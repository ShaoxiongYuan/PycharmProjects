# -*- coding: utf-8 -*-
import scrapy


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/cq/buy/']

    def parse(self, response):
        li_list = response.xpath('//ul[contains(@class,"carlist")]/li')
        for li in li_list:
            item = {
                'name': li.xpath('./a[1]/@title').get(),
                'link': li.xpath('./a[1]/@href').get()
            }
            print(item)
