import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0'}
proxies = {
    'http': 'http://182.32.234.18:9999',
    'https': 'https://182.32.234.18:9999'
}

html = requests.get(url=url, headers=headers, timeout=5).text
print(html)
