from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://mail.qq.com')

i_node = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to.frame(i_node)

driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
driver.find_element_by_id('u').send_keys('2379773801@qq.com')
driver.find_element_by_id('p').send_keys('65460035maomao')
driver.find_element_by_id('login_button').click()
