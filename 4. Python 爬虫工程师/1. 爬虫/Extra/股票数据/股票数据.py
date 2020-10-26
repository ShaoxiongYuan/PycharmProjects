import pprint

import requests
import time
import csv

f = open('股票数据.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['股票代码', '股票名称', '当前价', '涨跌额', '涨跌幅/%', '年初至今/%', '成交量', '成交额', '换手率/%',
                                           '市盈率TTM', '股息率/%', '市值'])
csv_writer.writeheader()

for page in range(1, 53):
    time.sleep(1)
    url = 'https://xueqiu.com/service/v5/stock/screener/quote/list'
    date = round(time.time() * 1000)
    params = {
        'page': '{}'.format(page),
        'size': '30',
        'order': 'desc',
        'order_by': 'amount',
        'exchange': 'CN',
        'market': 'CN',
        'type': 'sha',
        '_': '{}'.format(date),
    }
    cookies = {
        'Cookie': 'acw_tc=2760824216007592794858354eb971860e97492387fac450a734dbb6e89afb; xq_a_token=636e3a77b735ce64db9da253b75cbf49b2518316; xqat=636e3a77b735ce64db9da253b75cbf49b2518316; xq_r_token=91c25a6a9038fa2532dd45b2dd9b573a35e28cfd; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYwMjY0MzAyMCwiY3RtIjoxNjAwNzU5MjY3OTEwLCJjaWQiOiJkOWQwbjRBWnVwIn0.bengzIpmr0io9f44NJdHuc_6g9EIjtrSlMgnqwKSWVzI4syI_yIH1F-GJfK4bTelWzDirufjWMW9DfDMyMkI75TpJqiwIq8PRsa1bQ7IuCXLbN71ebsiTOGfA5OsWSPQOdVXQA0goqC4yvXLOk5KgC5FQIzZut0N4uaRDLsq7vhmcb8CBw504tCZnbIJTfGGIFIfw7TkwuUCXGY6Q-0mlOG8U4EUTcOCuxN87Ej_OIKnXN8cTSVh7XW6SFxOgU6p3yUXDgvS04rt-nFewpNNqfbGAKk965N-HJ9Mq8E52BRJ3rt_ndYP8yCaeQ6xSsz5P2mNlKwNFe9EQeltim_mDg; u=501600759279498; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1600759286; _ga=GA1.2.2049292015.1600759388; _gid=GA1.2.391362708.1600759388; s=du11eogy79; __utma=1.2049292015.1600759388.1600759397.1600759397.1; __utmc=1; __utmz=1.1600759397.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.3.10.1600759397; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1600759448'
    }
    headers = {
        'Host': 'xueqiu.com',
        'Pragma': 'no-cache',
        'Referer': 'https://xueqiu.com/hq',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    response = requests.get(url=url, params=params, headers=headers, cookies=cookies)
    html_data = response.json()
    data_list = html_data['data']['list']
    for i in data_list:
        dit = {'股票代码': i['symbol'], '股票名称': i['name'], '当前价': i['current'], '涨跌额': i['chg'], '涨跌幅/%': i['percent'],
               '年初至今/%': i['current_year_percent'], '成交量': i['volume'], '成交额': i['amount'], '换手率/%': i['turnover_rate'],
               '市盈率TTM': i['pe_ttm'], '股息率/%': i['dividend_yield'], '市值': i['market_capital']}
        csv_writer.writerow(dit)

        print(dit)

f.close()
