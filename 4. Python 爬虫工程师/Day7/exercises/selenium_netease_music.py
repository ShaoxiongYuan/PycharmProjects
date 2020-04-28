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
name_list = driver.find_elements_by_xpath('//tr/td[2]/div/div/div/span/a/b')
singer_list = driver.find_elements_by_xpath('//tr/td[4]/div')

# 写入数据库和json
for i in range(100):
    item = {
        '_id': i + 1,
        'name': name_list[i].get_attribute('title').replace('\xa0', ''),
        'singer': singer_list[i].get_attribute('title')
    }
    print(item)
    all_music.append(item)

myset.insert_many(all_music)
with open('netease_music.json', 'w', encoding='utf-8') as f:
    json.dump(all_music, f, ensure_ascii=False)
