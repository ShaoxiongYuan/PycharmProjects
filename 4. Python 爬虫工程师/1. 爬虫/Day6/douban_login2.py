import requests


def login():
    url = 'https://www.douban.com/people/196138324/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    }
    # 处理cookie为字典
    cookies_str = 'll="108309"; bid=8_ztaMM3JIM; push_noty_num=0; push_doumail_num=0; __yadk_uid=3hmqGZOkifjkuwU3FT6eKhLJ78D7rzhs; douban-profile-remind=1; douban-fav-remind=1; dbcl2="196138324:0VkXKE0NUAU"'
    cookies = get_cookies(cookies_str)
    # 确认html
    html = requests.get(url=url, headers=headers, cookies=cookies).text
    print(html)


def get_cookies(cookie):
    cookies = {}
    for kv in cookie.split('; '):
        key = kv.split('=')[0]
        value = kv.split('=')[1]
        cookies[key] = value
    return cookies


login()
