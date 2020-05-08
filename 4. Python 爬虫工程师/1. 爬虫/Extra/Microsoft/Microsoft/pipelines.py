# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.pipelines.files import FilesPipeline


class MicrosoftPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        url = item['template_url']
        yield scrapy.Request(url=url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        filename = '{}/{}{}'.format(item['title'], item['info_title'], os.path.splitext(url)[1])
        return filename
