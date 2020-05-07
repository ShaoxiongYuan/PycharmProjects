import time

from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://fanyi.youdao.com/')
while True:
    word = input('请输入需要翻译的词:')
    driver.find_element_by_xpath('//*[@id="inputOriginal"]').clear()
    driver.find_element_by_xpath('//*[@id="inputOriginal"]').send_keys(word)
    time.sleep(1)
    result = driver.find_element_by_xpath('//*[@id="transTarget"]/p/span').text
    print(result)
