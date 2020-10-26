import requests  # 第三方工具
import parsel  # 数据解析工具  (css\正则表达式\xpath)
import csv

f = open('NBA.csv', mode='a', encoding='utf-8', newline='')
csv_write = csv.DictWriter(f, fieldnames=['排名', '球员', '球队', '得分', '命中-出手', '命中率',
                                          '命中-三分', '三分命中率', '命中-罚球', '罚球命中率',
                                          '场次', '上场时间', ])

csv_write.writeheader()  # 写入表头

for page in range(1, 4):
    print('========================正在爬取第{}页数据======================='.format(page))
    # 1.确定url地址(网页分析)  完成一半  (静态网页\动态网页)
    url = 'https://nba.hupu.com/stats/players/pts/{}'.format(page)

    # 2.发送网络请求 requests(js\html\css)
    response = requests.get(url=url)
    # print(response)
    html_data = response.text
    # print(html_data)

    # 3.数据解析(筛选数据)
    # 3.1 转换数据类型
    selector = parsel.Selector(html_data)
    trs = selector.xpath('//tbody/tr[not(@class="color_font1 bg_a")]')
    for tr in trs:
        rank = tr.xpath('./td[1]/text()').get()  # 排名
        player = tr.xpath('./td[2]/a/text()').get()  # 球员
        team = tr.xpath('./td[3]/a/text()').get()  # 球队
        score = tr.xpath('./td[4]/text()').get()  # 得分
        hit_shot = tr.xpath('./td[5]/text()').get()  # 命中-出手
        hit_rate = tr.xpath('./td[6]/text()').get()  # 命中率
        hit_three = tr.xpath('./td[7]/text()').get()  # 命中-三分
        three_rate = tr.xpath('./td[8]/text()').get()  # 三分命中率
        hit_penalty = tr.xpath('./td[9]/text()').get()  # 命中-罚球
        penalty_rate = tr.xpath('./td[10]/text()').get()  # 罚球命中率
        session = tr.xpath('./td[11]/text()').get()  # 场次
        playing_time = tr.xpath('./td[12]/text()').get()  # 上场时间
        print(rank, player, team, score, hit_shot, hit_rate, hit_three,
              three_rate, hit_penalty, penalty_rate, session, playing_time)

        data_dict = {
            '排名': rank, '球员': player, '球队': team, '得分': score,
            '命中-出手': hit_shot, '命中率': hit_rate, '命中-三分': hit_three, '三分命中率': three_rate,
            '命中-罚球': hit_penalty, '罚球命中率': penalty_rate, '场次': session, '上场时间': playing_time}

        csv_write.writerow(data_dict)

f.close()  # 关闭文件
