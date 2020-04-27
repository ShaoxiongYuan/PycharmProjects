from selenium import webdriver
import time

url = 'https://maoyan.com/board/4'
browser = webdriver.Chrome()
browser.get(url)


def get_data():
    li_list = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for li in li_list:
        info_list = li.text.split('\n')
        item = {
            'number': info_list[0],
            'name': info_list[1],
            'star': info_list[2],
            'time': info_list[3],
            'score': info_list[4]
        }

        print(item)


while True:
    get_data()
    try:
        browser.find_element_by_link_text('下一页').click()
        time.sleep(2)
    except Exception as e:
        print('恭喜你!抓取结束')
        browser.quit()
        break
