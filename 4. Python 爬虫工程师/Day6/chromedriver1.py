from selenium import webdriver
import time

browser = webdriver.Chrome()
# browser.maximize_window()
browser.get('http://www.baidu.com')
browser.save_screenshot('baidu.png')
time.sleep(3)
browser.quit()
