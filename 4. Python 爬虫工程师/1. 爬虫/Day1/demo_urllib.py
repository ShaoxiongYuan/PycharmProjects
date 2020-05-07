from urllib import parse

params = {
    'wd': '祁天暄'
}

print(f'http://www.baidu.com/s?{parse.urlencode(params)}')
print('http://www.baidu.com/s?{}'.format(parse.urlencode(params)))
print('http://www.baidu.com/s?' + parse.urlencode(params))
print('http://www.baidu.com/s?%s' % parse.urlencode(params))
