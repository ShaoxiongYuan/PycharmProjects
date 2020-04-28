from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://mail.163.com')

driver.find_element_by_id('switchAccountLogin').click()

i_node = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(i_node)

driver.find_element_by_class_name('j-inputtext.dlemail.j-nameforslide').send_keys('yshaoxiong20')
driver.find_element_by_xpath('//*[@class="j-inputtext dlpwd"]').send_keys('SxiongY2019@')
driver.find_element_by_link_text('登  录').click()
