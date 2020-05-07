# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import PornhubItem


class PornhubSpider(scrapy.Spider):
    name = 'pornhub'
    allowed_domains = ['www.pornhub.com']
    start_urls = ['https://www.pornhub.com/']

    def parse(self, response):
        html = response.text
        pattern = r'<li class="pcVideoListItem.*?<a href="(.*?)".*?</a>'
        pattern = re.compile(pattern, re.S)
        res = pattern.findall(html)
        for item in res:
            yield scrapy.Request(url='https://www.pornhub.com' + item, callback=self.get_detail)

    def get_detail(self, response):
        item = PornhubItem()
        item['video_title'] = response.xpath('//div[@class="video-action-tab download-tab"]/div/a[3]/@download').get()
        item['video_url'] = response.xpath('//div[@class="video-action-tab download-tab"]/div/a[3]/@href').get()
        if item['video_title'] is not None and item['video_url'] is not None:
            yield item
