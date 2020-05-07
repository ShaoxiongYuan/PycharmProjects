"""
访问云打码官网,识别验证码图片
"""
from selenium import webdriver
from ydmapi import get_result
from PIL import Image


class YdmSpider:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get('http://www.yundama.com/')

    def get_image(self):
        """
        获取验证码图片(截取出来)
        :return:
        """
        # 1、获取官网屏幕截图
        self.browser.save_screenshot('index.png')
        # 2、截取验证码图片
        # location: 获取某个节点左上角的坐标（x、y坐标）
        location = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').location
        # size: 获取节点的大小（宽度和高度）
        size = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').size
        # 四个坐标: 记住 x y width height
        left_x = location['x']
        left_y = location['y']
        right_x = left_x + size['width']
        right_y = left_y + size['height']
        # 开始截图
        img = Image.open('index.png').crop((left_x, left_y, right_x, right_y))
        img.save('verify.png')

    def get_verify(self):
        """
        用在线打码获取验证结果
        :return:
        """
        result = get_result('verify.png')
        print('识别结果:', result)

    def run(self):
        """程序入口函数"""
        self.get_image()
        self.get_verify()
        # self.browser.close()


if __name__ == '__main__':
    spider = YdmSpider()
    spider.run()
