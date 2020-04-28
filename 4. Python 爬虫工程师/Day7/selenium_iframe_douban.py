from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.douban.com/')
i_node = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame(i_node)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_id('username').send_keys('13368226964')
driver.find_element_by_id('password').send_keys('65460035')
driver.find_element_by_link_text('登录豆瓣').click()
