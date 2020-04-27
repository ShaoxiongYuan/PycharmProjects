import requests
import execjs


class BaiduTranslateSpider:
    def __init__(self):
        self.url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.headers = {
            'Cookie': 'BIDUPSID=FBE6F9B0F21EC94EE4F697E1B1AEC849; PSTM=1587689823; BAIDUID=FBE6F9B0F21EC94EF52256741DF496D5:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1587785689; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; CHINA_PINYIN_SWITCH=0; DOUBLE_LANG_SWITCH=0; BDUSS=ZhRVdxcVdDU2pFWDkxVGw1cUY1c3R2WHBMQzNsU0I1Tn56dWViUkUxTGZXOHRlRVFBQUFBJCQAAAAAAAAAAAEAAAAqmQ9p1KzJ3NDbysfO0gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN~Oo17fzqNeYT; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1587793634; yjs_js_security_passport=bee26680be7119613dcb97b064eef2c515545772_1587793663_js',
            'Referer': 'https://fanyi.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'
        }

    def get_sign(self, word):
        with open('baidu_translate.js') as f:
            js_code = f.read()

        loader = execjs.compile(js_code)
        sign = loader.call('e', word)
        return sign

    def translate(self, word):
        sign = self.get_sign(word)
        data = {
            "from": "en",
            "to": "zh",
            "query": word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "b36e014bec2de66ae3c2d53b46c94b7a",
            "domain": "common"
        }
        html = requests.post(url=self.url, data=data, headers=self.headers).json()
        result = html['trans_result']['data'][0]['dst']
        print(result)

    def run(self):
        while True:
            word = input('单词：')
            self.translate(word)


if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    spider.run()
