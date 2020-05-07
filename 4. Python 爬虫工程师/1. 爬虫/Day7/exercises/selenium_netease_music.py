import time
from selenium import webdriver
import pymongo
import json

# 连接MongoDB
conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = conn['netease_db']
myset = db['musicset']
all_music = []

# 打开无头Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://music.163.com/#/discover/toplist')

# 进入iframe
node = driver.find_element_by_xpath('//iframe[1]')
driver.switch_to.frame(node)
time.sleep(1)

# 找到歌手和歌名
tr_list = driver.find_elements_by_xpath('//tbody/tr')

for i, tr in enumerate(tr_list):
    item = {
        '_id': i + 1,
        'name': tr.find_element_by_xpath('./td[2]/div/div/div/span/a/b').get_attribute('title').replace('\xa0', ''),
        'singer': tr.find_element_by_xpath('./td[4]/div').get_attribute('title')
    }
    print(item)
    all_music.append(item)

# 写入数据库和json
# myset.insert_many(all_music)
with open('netease_music.json', 'w', encoding='utf-8') as f:
    json.dump(all_music, f, ensure_ascii=False)

driver.quit()
