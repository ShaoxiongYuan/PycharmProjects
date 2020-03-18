from flask import Flask, request, render_template
import json

list_names = []
app = Flask(__name__)


@app.route('/post', methods=['GET', 'POST'])
def view1():
    if request.method == 'GET':
        return render_template('demo01.html')
    elif request.method == 'POST':
        uname = request.form.get('uname')
        return '欢迎%s' % uname


@app.route('/demo2')
def view2():
    return render_template('demo02.html')


@app.route('/demo2_server')
def server2():
    dict = {"name": "laowang", "age": 18}
    return json.dumps(dict, separators=(',', ':'), sort_keys=True)


@app.route('/demo3')
def demo3_view():
    return render_template('demo03.html')


@app.route('/demo3_server')
def server3():
    uname = request.args.get('uname')
    if uname in list_names:
        return '0'
    else:
        list_names.append(uname)
        return '1'


@app.route('/register', methods=['POST'])
def register():
    uname = request.form.get('uname')
    pwd = request.form.get('pwd')
    return '注册成功' + uname + pwd


if __name__ == '__main__':
    app.run(debug=True)
