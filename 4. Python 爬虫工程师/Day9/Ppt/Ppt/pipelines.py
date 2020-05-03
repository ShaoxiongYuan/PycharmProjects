# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
import scrapy
import os


class PptPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['ppt_download'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        filename = '{}/{}{}'.format(
            item['parent_name'],
            item['ppt_name'],
            os.path.splitext(request.url)[1])

        return filename
