# -*- coding: utf-8 -*-
import scrapy
from ..items import PptItem


class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/xiazai/']

    def parse(self, response):
        """
        一级页面解析函数
        :param response:
        :return:
        """
        li_list = response.xpath('//div[@class="col_nav clearfix"]/ul/li')
        for li in li_list[1:]:
            item = PptItem()
            item['parent_name'] = li.xpath('./a/text()').get()
            parent_url = 'http://www.1ppt.com' + li.xpath('./a/@href').get()
            yield scrapy.Request(
                url=parent_url,
                meta={'meta1': item, 'parent_url': parent_url},
                callback=self.get_total_page
            )

    def get_total_page(self, response):
        meta1 = response.meta['meta1']
        parent_url = response.meta['parent_url']
        try:
            last_page_href = response.xpath('//ul[@class="pages"]/li[last()]/a/@href').get()
            total = int(last_page_href.split('.')[0].split('_')[-1])
            # 拼接多页URL
            for page in range(1, total + 1):
                # http://www.1ppt.com/xiazai/zongjie/ppt_zongjie_1.html
                page_url = parent_url + '_'.join(last_page_href.split('.')[0].split('_')[:-1]) + '_' + str(
                    page) + '.html'
                yield scrapy.Request(url=page_url, meta={'meta2': meta1}, callback=self.get_ppt_info)
        except Exception as e:
            yield scrapy.Request(url=parent_url, meta={'meta2': meta1}, callback=self.get_ppt_info, dont_filter=True)

    def get_ppt_info(self, response):
        """
        PPT名字和URL
        :param response:
        :return:
        """
        meta2 = response.meta['meta2']
        li_list = response.xpath('//ul[@class="tplist"]/li')
        for li in li_list:
            item = PptItem()
            item['ppt_name'] = li.xpath('./h2/a/text()').get()
            item['parent_name'] = meta2['parent_name']
            son_url = 'http://www.1ppt.com' + li.xpath('./a/@href').get()
            yield scrapy.Request(url=son_url, meta={'item': item}, callback=self.get_download_url)

    def get_download_url(self, response):
        """
        提取下载链接r
        :param response:
        :return:
        """
        item = response.meta['item']
        item['ppt_download'] = response.xpath('//ul[@class="downurllist"]/li/a/@href').get()
        yield item
