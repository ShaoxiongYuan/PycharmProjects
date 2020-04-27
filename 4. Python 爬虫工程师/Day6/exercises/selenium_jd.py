import time
from selenium import webdriver

keyword = input('需要查找的商品:')
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.jd.com/')
browser.find_element_by_xpath('//*[@id="key"]').send_keys(keyword)
browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()


def get_data():
    browser.execute_script(
        'window.scrollTo(0,document.body.scrollHeight)'
    )
    time.sleep(2)
    goods_list = browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
    for good in goods_list:
        item = {
            'name': good.find_element_by_xpath('.//div[@class="p-name"]/a/em').text,
            'price': good.find_element_by_xpath('.//div[@class="p-price"]').text,
            'comment': good.find_element_by_xpath('.//div[@class="p-commit"]/strong').text,
            'publication': good.find_element_by_xpath('.//div[@class="p-shopnum"]').text
        }
        print(item)
        print('*' * 50)


while True:
    get_data()
    if browser.page_source.find('pn-next disabled') == -1:
        browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
    else:
        browser.quit()
        break
