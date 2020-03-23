from flask import Flask, render_template, request

list_names = []
advice = {
    'python': ['python能做什么', 'python书籍', 'python官网', 'python教程'],
    'pycharm': ['pycharm官网', 'jetbrains', 'intellij idea', '其他编译工具'],
    '股票': ['股票定义', '股票怎么玩', '股票开户基本知识', '股票行情', '美股暴跌'],
    '疫情': ['COVID-19', '新冠肺炎', '疫情分布地图', '意大利疫情人数', '特朗普极端言论']
}

app = Flask(__name__)


@app.route('/demo')
def demo_view():
    return render_template('demo01.html')


@app.route('/exer1')
def exer1_view():
    return render_template('exercise01.html')


@app.route('/exer2')
def exer2_view():
    return render_template('exercise02.html')


@app.route('/exer3')
def exer3_view():
    return render_template('exercise03.html')


@app.route('/server')
def server_view():
    return '接收前端AJAX请求成功'


@app.route('/exer_server')
def server1():
    uname = request.args.get('uname')
    return "欢迎%s" % uname


@app.route('/exer2_server')
def server2():
    uname = request.args.get('uname')
    if uname in list_names:
        return '0'
    else:
        list_names.append(uname)
        return '1'


@app.route('/exer3_server')
def server3():
    keyword = request.args.get('keyword')
    str_item = ''
    for k, v in advice.items():
        if k == keyword:
            for i in v:
                str_item += i + '<br>'
            break
    return str_item


if __name__ == '__main__':
    app.run(debug=True)
