from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://bais.com.cn/assets.html')
browser.find_element_by_xpath('//ul/li[4]/a').click()
titles = browser.find_elements_by_xpath('//ul[@class="list-group"]/li')

for i in range(len(titles)):
    browser.find_element_by_xpath('//ul[@class="list-group"]/li[{}]/a'.format(i + 1)).click()
    all_win = browser.window_handles
    browser.switch_to.window(all_win[-1])
    browser.close()
    browser.switch_to.window(all_win[0])
