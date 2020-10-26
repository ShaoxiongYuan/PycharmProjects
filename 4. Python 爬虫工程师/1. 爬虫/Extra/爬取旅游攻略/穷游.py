import csv
import requests
import parsel

for page in range(1, 172):
    print('================================正在爬取第{}页数据================================'.format(page))
    url = 'https://place.qyer.com/china/citylist-0-0-{}/'.format(str(page))
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response = requests.get(url=url, headers=headers)
    html_data = response.text
    # print(html_data)

    selector = parsel.Selector(html_data)
    lis = selector.xpath('//ul[@class="plcCitylist"]/li')

    for li in lis:
        travel_place = li.xpath('.//h3/a/text()').get()  # 目的地
        travel_people = li.xpath('.//p[@class="beento"]/text()').get()  # 去过的人数

        travel_hot = li.xpath('.//p[@class="pois"]/a/text()').getall()  # 热门景点
        travel_hot = [hot.strip() for hot in travel_hot]
        travel_hot = '、'.join(travel_hot)

        travel_url = li.xpath('.//h3/a/@href').get()  # 目的地详情页url
        travel_imgUrl = li.xpath('./p/a/img/@src').get()  # 目的地详情页url
        print(travel_place, travel_people, travel_hot, travel_url, travel_imgUrl, sep=' | ')

        with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([travel_place, travel_people, travel_hot, travel_url, travel_imgUrl])
