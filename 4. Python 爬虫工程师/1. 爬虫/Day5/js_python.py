import execjs

js_code = open('hello.js').read()

loader = execjs.compile(js_code)
print(loader.call('test', '赵敏'))
