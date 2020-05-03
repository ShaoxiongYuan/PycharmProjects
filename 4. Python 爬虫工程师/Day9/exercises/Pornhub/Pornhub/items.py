# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PornhubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_url = scrapy.Field()
    video_title = scrapy.Field()
