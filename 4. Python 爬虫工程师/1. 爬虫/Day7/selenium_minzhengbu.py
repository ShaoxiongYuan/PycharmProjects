import sys
import redis
from selenium import webdriver
import time
import hashlib


class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def parse_html(self):
        a_node = self.driver.find_element_by_partial_link_text('中华人民共和国县以上行政区划代码')
        href = a_node.get_attribute('href')
        finger = self.md5_url(href)
        if self.r.sadd('county:spider', finger) == 1:
            a_node.click()
            time.sleep(1)
            all_win = self.driver.window_handles
            self.driver.switch_to.window(all_win[1])

            tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
            for tr in tr_list:
                item = {
                    'name': tr.find_element_by_xpath('./td[3]').text.strip(),
                    'code': tr.find_element_by_xpath('./td[2]').text.strip()
                }
                print(item)
        else:
            self.driver.quit()
            sys.exit('完成')

    def md5_url(self, url):
        s = hashlib.md5()
        s.update(url.encode())
        return s.hexdigest()

    def run(self):
        self.parse_html()


if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()
