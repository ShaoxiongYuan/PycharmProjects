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
        return json.dumps({"code": 0, "msg": "用户名已存在"})
    else:
        list_names.append(uname)
        return json.dumps({"code": 1, "msg": "OK"})


@app.route('/register', methods=['POST'])
def register():
    uname = request.json.get('uname')
    pwd = request.json.get('pwd')
    return '注册成功' + uname + pwd


@app.route('/data')
def data():
    return render_template('exercise01.html')


@app.route('/data_server')
def data_server():
    cartdata = {
        "username": "dongdong",
        "cart": [
            {
                "id": "1",
                "count": "11",
                "name": "蓝色小尺寸",
                "default_image_url": "2_5pdezhv.jpg",
                "price": 100,
                "selected": True,
                "sku_sale_attr_name": ["安踏A/尺寸：", "安踏A/颜色："],
                "sku_sale_attr_val": ["15寸", "蓝色"]
            },
            {
                "id": "2",
                "count": "9",
                "name": "红色大尺寸",
                "default_image_url": "3_JGA6F97.jpg",
                "price": 10000,
                "selected": True,
                "sku_sale_attr_name": ["安踏A/尺寸：", "安踏A/颜色："],
                "sku_sale_attr_val": ["18寸", "绿色"]
            },
            {
                "id": "3",
                "count": "10",
                "name": "蓝色小尺寸",
                "default_image_url": "4_z3FdRMq.jpg",
                "price": 1000,
                "selected": True,
                "sku_sale_attr_name": ["安踏B/尺寸：", "安踏B/颜色："],
                "sku_sale_attr_val": ["18寸", "蓝色"]
            }
        ]
    }
    return json.dumps(cartdata)


if __name__ == '__main__':
    app.run(debug=True)
