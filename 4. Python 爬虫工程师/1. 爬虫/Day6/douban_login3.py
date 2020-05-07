import requests

s = requests.session()


def login():
    post_url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = {
        'ck': 'xAcs',
        'name': '13368226964',
        'password': '65460035',
        'remember': 'false',
        'ticket': ''
    }
    headers = {
        "Cookie": 'll="108309"; bid=8_ztaMM3JIM; push_noty_num=0; push_doumail_num=0; douban-profile-remind=1; douban-fav-remind=1; apiKey=; last_login_way=account; ap_v=0,6.0; login_start_time=1587969581418',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'
    }
    s.post(url=post_url, headers=headers, data=data)
    get_url = 'https://www.douban.com/people/196138324/'
    get_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    html = s.get(url=get_url, headers=get_headers).text
    print(html)


login()
