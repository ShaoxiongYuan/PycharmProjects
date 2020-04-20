import requests
from urllib import parse

word = input('请输入搜索内容:')
params = parse.urlencode({'wd': word})
url = 'http://www.baidu.com/s?{}'.format(params)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
html = requests.get(url=url, headers=headers).text

with open(word + '.html', 'w', encoding='utf-8') as f:
    f.write(html)
