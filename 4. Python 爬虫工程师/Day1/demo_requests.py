import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'
}

res = requests.get(url=url, headers=headers)


print(res.text)
# print(res.content)
# print(res.url)
# print(res.status_code)
