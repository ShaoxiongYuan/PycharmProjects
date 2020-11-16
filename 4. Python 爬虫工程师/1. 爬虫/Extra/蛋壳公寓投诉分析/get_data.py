import pandas as pd
import requests
import time
from fake_useragent import UserAgent  # 生成随机请求头
import urllib3

urllib3.disable_warnings()


# uid请求数据，数据格式较为规范，方便处理
def request_data_uid(req_s, couid, page, total_page):
    params = {
        'couid': couid,  # 商家ID
        'type': '1',
        'page_size': page * 10,  # 每页10条
        'page': page,  # 第几页
    }
    print(f"正在爬取第{page}页，共计{total_page}页，剩余{total_page - page}页")
    url = 'https://tousu.sina.com.cn/api/company/received_complaints'

    # 伪造随机请求头
    header = {'User-Agent': UserAgent().random}
    res = req_s.get(url, headers=header, params=params, verify=False)
    #     res = requests.get(url, params=params, verify=False)
    info_list = res.json()['result']['data']['complaints']
    result = []
    for info in info_list:
        _data = info['main']

        # 投诉日期
        timestamp = float(_data['timestamp'])
        date = time.strftime("%Y-%m-%d", time.localtime(timestamp))

        # sn：投诉编号    title :投诉问题   appeal：投诉诉求   summary :问题说明
        data = [date, _data['sn'], _data['title'], _data['appeal'], _data['summary']]
        result.append(data)

    pd_result = pd.DataFrame(result, columns=["投诉日期", "投诉编号", "投诉问题", "投诉诉求", "详细说明"])
    return pd_result


# keywords请求数据，数据格式相对混乱
# 紫梧桐这种没有收录商家ID的公司只能用keywords进行检索处理
# 蛋壳公寓有uid的这种也可以使用keywods进行数据请求

def request_data_keywords(req_s, keyword, page, total_page):
    params = {
        'keywords': keyword,  # 检索关键词
        'type': '1',
        'page_size': page * 10,  # 每页10条
        'page': page,  # 第几页
    }
    print(f"正在爬取第{page}页，共计{total_page}页，剩余{total_page - page}页")
    # url = 'https://tousu.sina.com.cn/api/company/received_complaints'
    url = 'https://tousu.sina.com.cn/api/index/s?'

    # 伪造随机请求头
    header = {'user-agent': UserAgent().random}
    res = req_s.get(url, headers=header, params=params, verify=False)
    info_list = res.json()['result']['data']['lists']
    result = []
    for info in info_list:
        _data = info['main']

        # 投诉日期
        timestamp = float(_data['timestamp'])
        date = time.strftime("%Y-%m-%d", time.localtime(timestamp))

        # sn：投诉编号    title :投诉问题   appeal：投诉诉求   summary :问题说明
        data = [date, _data['sn'], _data['title'], _data['appeal'], _data['summary']]
        result.append(data)

    pd_result = pd.DataFrame(result, columns=["投诉日期", "投诉编号", "投诉问题", "投诉诉求", "详细说明"])
    return pd_result


# 生成并保持请求会话
req_s = requests.Session()

# 蛋壳公寓
result = pd.DataFrame()
total_page = 2507
for page in range(1, total_page + 1):
    data = request_data_uid(req_s, '5350527288', page, total_page)
    result = result.append(data)
result['投诉对象'] = "蛋壳公寓"
result.to_csv("data/蛋壳公寓投诉数据.csv", index=False)

# 紫梧桐 关键词检索
# 蛋壳公寓为品牌名，工商注册名称为紫梧桐资产管理有限公司
result = pd.DataFrame()
total_page = 56
for page in range(1, total_page + 1):
    data = request_data_keywords(req_s, '紫梧桐', page, total_page)
    result = result.append(data)
result['投诉对象'] = "紫梧桐"
result.to_csv("data/紫梧桐投诉数据.csv", index=False)
