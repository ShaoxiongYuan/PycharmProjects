# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MicrosoftItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    info_title = scrapy.Field()
    template_url = scrapy.Field()
