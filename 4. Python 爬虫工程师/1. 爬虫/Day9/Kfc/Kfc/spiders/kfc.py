# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import re
from ..items import KfcItem


class KfcSpider(scrapy.Spider):
    name = 'kfc'
    allowed_domains = ['www.kfc.com.cn']

    def start_requests(self):
        all_city = self.get_all_city()
        for city in all_city:
            total = self.get_total(city)
            for page in range(1, total + 1):
                post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
                formdata = {
                    'cname': city,
                    'pid': '',
                    'pageIndex': str(page),
                    'pageSize': '10'
                }
                yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.detail_page)

    def detail_page(self, response):
        html = json.loads(response.text)
        for kfc_shop in html['Table1']:
            item = KfcItem()
            item['row_num'] = kfc_shop['rownum']
            item['store_name'] = kfc_shop['storeName'].strip()
            item['address_detail'] = kfc_shop['addressDetail'].strip()
            item['city_name'] = kfc_shop['cityName'].strip()
            item['province_name'] = kfc_shop['provinceName'].strip()
            yield item

    def get_all_city(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'}
        url = 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
        html = requests.get(url=url, headers=headers).text
        regex = '<a href=".*?rel="(.*?)">'
        pattern = re.compile(regex, re.S)
        all_city = pattern.findall(html)
        return all_city

    def get_total(self, city):
        post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
        data = {
            'cname': city,
            'pid': '',
            'pageIndex': '1',
            'pageSize': '10'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'}
        html = requests.post(url=post_url, data=data, headers=headers).json()
        count = html['Table'][0]['rowcount']
        total = count // 10 if count % 10 == 0 else count // 10 + 1
        return total
