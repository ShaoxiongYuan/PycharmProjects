import os

import requests
from fake_useragent import UserAgent

url = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1249391358,3728112758&fm=26&gp=0.jpg'

headers = {'User-Agent': UserAgent().random}

html = requests.get(url=url, headers=headers).content

directory = './pictures/'
if not os.path.exists(directory):
    os.makedirs(directory)

filename = directory + url[-10:]
with open(filename, 'wb') as f:
    f.write(html)
