# -*- coding: utf-8 -*-
import scrapy
from ..items import MicrosoftItem


class MicrosoftSpider(scrapy.Spider):
    name = 'microsoft'
    allowed_domains = ['templates.office.com']
    start_urls = ['https://templates.office.com/']

    def parse(self, response):
        category_list = response.xpath('//p[@class="c-subheading-4"]')
        for category in category_list:
            item = MicrosoftItem()
            item['title'] = category.xpath('./a/text()').get()
            if category.xpath('./a/@href').get()[0] == '/':
                href = 'https://templates.office.com' + category.xpath('./a/@href').get()
            else:
                href = category.xpath('./a/@href').get()
            yield scrapy.Request(url=href, meta={'meta1': item, 'url': href}, callback=self.get_total)

    def get_total(self, response):
        url = response.meta['url']
        meta2 = response.meta['meta1']
        if response.xpath('//li/@data-label'):
            pages_list = response.xpath('//li/@data-label')
            for i in range(len(pages_list)):
                d_url = url + '?page=' + str(i + 1)
                yield scrapy.Request(url=d_url, meta={'meta2': meta2}, callback=self.parse_two_page, dont_filter=True)
        else:
            yield scrapy.Request(url=url, meta={'meta2': meta2}, callback=self.parse_two_page, dont_filter=True)

    def parse_two_page(self, response):
        meta2 = response.meta['meta2']
        info_list = response.xpath('//section')
        for info in info_list[:-1]:
            item = MicrosoftItem()
            item['info_title'] = info.xpath('./a/@data-bi-name').get()
            detail_url = 'https://templates.office.com' + info.xpath('./a/@href').get()
            item['title'] = meta2['title']
            yield scrapy.Request(url=detail_url, meta={'item': item}, callback=self.get_download_url)

    def get_download_url(self, response):
        meta2 = response.meta['item']
        download_url = response.xpath('//a[contains(@data-bi-name,"Download")]/@href').get()
        item = MicrosoftItem()
        item['template_url'] = download_url
        item['title'] = meta2['title']

        item['info_title'] = meta2['info_title']
        item['info_title'].replace('?', '').strip()
        yield item
