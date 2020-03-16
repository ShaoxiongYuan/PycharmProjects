from flask import Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "这是项目首页"


@app.route('/detail')
def detail():
    return "这是项目的详情页"


@app.route('/show/<name>')
def show(name):
    return "欢迎%s" % name


@app.route('/show/<name>/<int:age>')
def show2(name, age):
    return "姓名：%s，年龄：%s" % (name, age)


@app.route('/server', methods=['POST'])
def server():
    # args:接收GET请求的数据
    # uname = request.args['uname']

    # 接收POST请求的数据
    uname = request.form['uname']
    return "欢迎%s" % uname


if __name__ == '__main__':
    app.run(debug=True)
