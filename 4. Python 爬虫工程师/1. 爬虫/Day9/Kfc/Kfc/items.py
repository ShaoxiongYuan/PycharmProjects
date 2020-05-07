# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KfcItem(scrapy.Item):
    # define the fields for your item here like:
    row_num = scrapy.Field()
    store_name = scrapy.Field()
    address_detail = scrapy.Field()
    city_name = scrapy.Field()
    province_name = scrapy.Field()
