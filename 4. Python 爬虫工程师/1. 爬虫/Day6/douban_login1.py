import requests


def login():
    url = 'https://www.douban.com/people/196138324/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Cookie': 'll="108309"; bid=8_ztaMM3JIM; push_noty_num=0; push_doumail_num=0; __yadk_uid=3hmqGZOkifjkuwU3FT6eKhLJ78D7rzhs; douban-profile-remind=1; douban-fav-remind=1; dbcl2="196138324:0VkXKE0NUAU"'
    }
    html = requests.get(url=url, headers=headers).text
    # 查看html中是否包含个人主页的信息 - 比如搜索 "个人主页"
    print(html)


login()
