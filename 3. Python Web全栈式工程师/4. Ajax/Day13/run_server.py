from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/cross_server')
def cross_server():
    func_name = request.args.get('callback')
    return func_name + '("这是5001端口返回的数据")'


@app.route('/data_server')
def data_server():
    func_name = request.args.get('callback')
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
    response = json.dumps({"code": 200, "data": cartdata})
    return func_name + "(" + response + ")"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
