import csv

with open('spider.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Amy', 'Lily', 'Tom'])

with open('spider.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows([('聂风', '血饮狂刀'), ('圣斗士星矢', '天马流星拳')])
