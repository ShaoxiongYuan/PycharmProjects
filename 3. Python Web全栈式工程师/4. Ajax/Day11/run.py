from flask import Flask, render_template, request

list_names = []

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


if __name__ == '__main__':
    app.run(debug=True)
