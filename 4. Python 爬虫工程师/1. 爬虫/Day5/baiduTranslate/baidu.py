import execjs

with open('baidu_translate.js') as f:
    js_code = f.read()

loader = execjs.compile(js_code)
print(loader.call('e', 'hello'))
