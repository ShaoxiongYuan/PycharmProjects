from flask import Flask, request, render_template
import json
from time import sleep

app = Flask(__name__)


@app.route('/load')
def load():
    return render_template('demo01.html')


@app.route('/load_server', methods=['GET', 'POST'])
def load_server():
    # if request.method == 'GET':
    #     uname = request.args.get('uname')
    #     age = request.args.get('age')
    #     print(uname, age)
    # elif request.method == 'POST':
    #     uname = request.form.get('uname')
    #     age = request.form.get('age')
    #     print(uname, age)
    return render_template('demo01_server.html')


@app.route('/header')
def header_view():
    return render_template('header.html')


@app.route('/footer')
def footer_view():
    return render_template('footer.html')


@app.route('/get')
def get_view():
    return render_template('demo02.html')


@app.route('/get_server')
def get_server():
    uname = request.args.get('uname')
    age = int(request.args.get('age'))
    if age < 18:
        response = {"code": 200, "msg": 'Fail'}
        return json.dumps(response)
    else:
        response = {"code": 200, "msg": 'OK', 'uname': uname}
        return json.dumps(response)


@app.route('/post', methods=['GET', 'POST'])
def post_view():
    if request.method == 'GET':
        return render_template('demo03.html')
    elif request.method == 'POST':
        uname = request.form.get('uname')
        age = request.form.get('age')
        response = {"code": 200, "msg": '欢迎%s岁的%s' % (age, uname)}
        return json.dumps(response)


@app.route('/ajax')
def ajax_view():
    return render_template('demo04.html')


@app.route('/ajax_server', methods=['GET', 'POST'])
def ajax_server():
    if request.method == 'GET':
        sleep(3)
        return json.dumps({"code": 200, "msg": "OK"})
    elif request.method == 'POST':
        uname = request.json.get('uname')
        return json.dumps({"code": 200, "msg": '欢迎' + uname})


@app.route('/cross')
def cross():
    return render_template('demo05_cross.html')


@app.route('/cross1')
def cross1():
    return render_template('demo05_cross1.html')


@app.route('/cross2')
def cross2():
    return render_template('demo05_cross2.html')


@app.route('/data')
def data_view():
    return render_template('exercise01.html')


if __name__ == '__main__':
    app.run(debug=True)
