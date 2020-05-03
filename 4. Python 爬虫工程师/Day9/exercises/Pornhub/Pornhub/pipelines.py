# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.media import MediaPipeline
import scrapy


class PornhubPipeline(MediaPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['video_url'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        title = request.meta['item']['video_title']
        filename = '{}.mp4'.format(title)
        return filename


class PornhubPipeline1:
    def process_item(self, item, spider):
        print(dict(item))
        return item
