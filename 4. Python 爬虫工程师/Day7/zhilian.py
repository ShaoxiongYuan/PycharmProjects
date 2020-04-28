import time
from selenium import webdriver

keyword = input('需要查找的商品:')
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://i.zhaopin.com/')
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[5]/div/div/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="rightNav_top"]/div/div[2]/div/div/div[2]/div/div[1]/input').send_keys(keyword)
browser.find_element_by_xpath('//*[@id="rightNav_top"]/div/div[2]/div/div/div[2]/div/button').click()
