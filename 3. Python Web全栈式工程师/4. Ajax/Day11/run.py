from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/demo')
def demo_view():
    return render_template('demo01.html')


@app.route('/demo2')
def exer1_view():
    return render_template('exercise01.html')


@app.route('/server')
def server_view():
    return '接收前端AJAX请求成功'


@app.route('/exer_server')
def server2():
    uname = request.args.get('uname')
    return uname


if __name__ == '__main__':
    app.run(debug=True)
