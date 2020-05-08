# -*- coding: utf-8 -*-
import scrapy
from ..items import WechatItem


class WechatSpider(scrapy.Spider):
    name = 'wechat'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = [
        'https://mp.weixin.qq.com/s?__biz=MjM5NzU0MzU0Nw==&mid=2651384815&idx=1&sn=726f7dc73447c9a87f2da1c0b321d06d&chksm=bd2420fb8a53a9ed58a831761aab37085d69b6f345a44b73625b428b0e121f54fb568009e2c0&scene=126&sessionid=1588829283&key=2edb9e4f1ac19867cca7acbbc9a54991f1a5f4db8b0b66c011510519a0918a24caa617bdf9b7eae9b20e99f04520167e7f2f46c0168f34a2d2613c7b16a9f23723f5df80c52657dbd5f5ac5f558a4aa5&ascene=1&uin=NjIzNTU3NjE3&devicetype=Windows+10+x64&version=62090072&lang=en&exportkey=A%2BZXZgVynaQZeDr%2BFEoWlWo%3D&pass_ticket=1DgIbHiyh4peY%2FhsWr67EEyl2ecK3bu8WPFEoRoGHFPDmk9dWiVMNdlHm8VXlww3']
    count = 0

    def parse(self, response):
        img_list = response.xpath('//img')
        for img in img_list[1:]:
            item = WechatItem()
            item['title'] = str(self.count)
            item['img_url'] = img.xpath('./@data-src').get()
            self.count += 1
            yield item
