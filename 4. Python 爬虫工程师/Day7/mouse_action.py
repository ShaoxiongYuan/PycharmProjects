from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com/')

node = driver.find_element_by_xpath('//*[@id="u1"]/a[9]')
ActionChains(driver).move_to_element(to_element=node).perform()

driver.find_element_by_link_text('高级搜索').click()
