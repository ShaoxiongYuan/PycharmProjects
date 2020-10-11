import requests
import parsel
import csv

f = open('4399游戏.csv', mode='a', encoding='utf-8-sig', newline='')

csv_writer = csv.DictWriter(f, fieldnames=['游戏地址', '游戏名字'])
csv_writer.writeheader()
for page in range(1, 106):
    url = 'http://www.4399.com/flash_fl/5_{}.htm'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    selector = parsel.Selector(response.text)
    lis = selector.css('#classic li')
    for li in lis:
        dit = {}
        data_url = li.css('a::attr(href)').get()
        new_url = 'http://www.4399.com' + data_url.replace('http://', '/')
        dit['游戏地址'] = new_url
        title = li.css('img::attr(alt)').get()
        dit['游戏名字'] = title
        print(new_url, title)
        csv_writer.writerow(dit)
f.close()
