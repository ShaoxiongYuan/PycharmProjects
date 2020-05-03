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
            yield scrapy.Request(url=url, callback=self.parse_one_page, cookies=self.get_cookies())

    def parse_one_page(self, response):
        li_list = response.xpath('//ul[contains(@class,"carlist")]/li')
        for li in li_list:
            item = GuaziItem()
            item['name'] = li.xpath('./a[1]/@title').get()
            item['link'] = 'https://www.guazi.com' + li.xpath('./a[1]/@href').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()

            yield scrapy.Request(url=item['link'], meta={'item': item}, cookies=self.get_cookies(),
                                 callback=self.parse_two_page)

    def parse_two_page(self, response):
        item = response.meta['item']
        item['km'] = response.xpath('//ul[@class="assort clearfix"]/li[2]/span/text()').get()
        item['displace'] = response.xpath('//ul[@class="assort clearfix"]/li[3]/span/text()').get()
        item['typ'] = response.xpath('//ul[@class="assort clearfix"]/li[4]/span/text()').get()

        yield item

    def get_cookies(self):
        cook_str = '=uuid=0461581f-1593-43eb-f070-0025fabd5f16; cityDomain=cq; ganji_uuid=8211876012728113518430; lg=1; antipas=2141L224hn4f24Zv7xP4d098R; clueSourceCode=%2A%2300; user_city_id=15; preTime=%7B%22last%22%3A1588234244%2C%22this%22%3A1588066476%2C%22pre%22%3A1588066476%7D; sessionid=6ca82eb4-57c3-4dd3-c6ca-d7510c52a366; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%220461581f-1593-43eb-f070-0025fabd5f16%22%2C%22ca_city%22%3A%22cq%22%2C%22sessionid%22%3A%226ca82eb4-57c3-4dd3-c6ca-d7510c52a366%22%7D; close_finance_popup=2020-04-30; lng_lat=106.480282_29.56301; gps_type=1'
        cookies = {}
        for kv in cook_str.split('; '):
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookies[key] = value

        return cookies
