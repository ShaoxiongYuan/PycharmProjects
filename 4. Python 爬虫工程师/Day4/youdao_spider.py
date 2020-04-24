"""
抓取有道翻译结果
"""
import requests
import time
import random
import hashlib


class YDSpider:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Connection": "keep-alive",
            "Content-Length": "241",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-2125119731@10.108.160.17; JSESSIONID=aaa7sLO2hDxidgekB7Qgx; OUTFOX_SEARCH_USER_ID_NCOO=1112786950.333426; ___rl__test__cookies=1587717107130",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

    def get_ts_salt_sign(self, word):
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        string = "fanyideskweb" + word + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        s = hashlib.md5()
        s.update(string.encode())
        sign = s.hexdigest()
        return ts, salt, sign

    def get_result(self, word):
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "zh-CHS",
            "to": "ja",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "f9c86b1fdf2f53c1fefaef343285247b",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        html = requests.post(url=self.url, data=data, headers=self.headers).json()
        result = html['translateResult'][0][0]['tgt']
        print(result)

    def run(self):
        while True:
            word = input('需要查询的单词：')
            self.get_result(word)


if __name__ == '__main__':
    spider = YDSpider()
    spider.run()
