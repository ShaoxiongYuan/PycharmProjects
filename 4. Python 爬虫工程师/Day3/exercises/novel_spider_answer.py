import requests
import re
import time
import random


class NovelSpider(object):
    def __init__(self):
        # 主页的URL地址
        self.url = 'http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

    def get_html(self, url):
        """功能函数1 - 获取html"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def re_func(self, regex, html):
        """功能函数2 - 正则解析"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_one_page(self, one_url):
        """一级页面解析函数：提取小说链接"""
        one_html = self.get_html(url=one_url)
        regex = '<div class="bookname">.*?href="(.*?)".*?</div>'
        # one_link_list: [当页所有小说的链接]
        one_link_list = self.re_func(regex, one_html)
        for one_link in one_link_list:
            # 将此小说的内容所有章节内容获取到
            self.get_novel(one_link)

    def get_novel(self, one_link):
        """此函数总功能：获取1个小说的所有章节内容"""
        two_html = self.get_html(url=one_link)
        # 从开始阅读节点获取到小说具体内容的链接
        regex = """<div class="btn-group">.*?href="(.*?)".*?</div>"""
        two_link_list = self.re_func(regex, two_html)
        two_link = two_link_list[0] if two_link_list else None
        # 解析并提取此小说目录链接
        if two_link:
            self.get_novel_directory(two_link)

    def get_novel_directory(self, two_link):
        """提取此小说目录链接"""
        directory_html = self.get_html(url=two_link)
        regex = '<div class="chap_btnbox">.*?<a href="(.*?)".*?>目录</a>'
        directory_link_list = self.re_func(regex, directory_html)
        directory_link = directory_link_list[0] if directory_link_list else None
        # 获取小说名称
        regex_name = '<body.*?bookName="(.*?)"'
        name_list = self.re_func(regex_name, directory_html)
        novel_name = name_list[0] if name_list else None
        print(novel_name)
        if directory_link and novel_name:
            # 获取具体章节的目录链接
            self.get_all_link(directory_link, novel_name)

    def get_all_link(self, directory_link, novel_name):
        """获取具体章节的目录链接"""
        directory_html = self.get_html(url=directory_link)
        regex = '<li class=" col-4">.*?<a  href="(.*?)".*?</a>'
        novel_text_link_list = self.re_func(regex, directory_html)

        for novel_text_link in novel_text_link_list:
            # 获取具体小说章节内容
            novel_text = self.get_novel_content(novel_text_link)
            time.sleep(random.randint(1, 2))

    def get_novel_content(self, novel_text_link):
        """获取具体小说章节内容"""
        novel_text_html = self.get_html(url=novel_text_link)
        regex = '<div class="content".*?>(.*?)</div>'
        novel_text = re.findall(regex, novel_text_html, re.S)[0].replace('<p>', '').replace('</p>', '\n')
        print(novel_text)
        return novel_text

    # 程序入口函数
    def run(self):
        for p in range(1, 967):
            url = self.url.format(p)
            self.parse_one_page(url)


if __name__ == '__main__':
    spider = NovelSpider()
    spider.run()
