import json
import time

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def server():
    size = request.args.get('size')
    with open('comment.data') as f:
        all_data = json.loads(f.read())
        if not size:
            data = all_data[0:10]
        else:
            size = int(size)
            data = all_data[size:size + 10]
    if data:
        return json.dumps({"code": 200, "data": data})
    else:
        return json.dumps({"code": 201, "error": "没有数据了"})


@app.route('/add', methods=['POST'])
def add():
    name = request.json.get('name')
    content = request.json.get('content')
    with open('comment.data', 'r') as f:
        all_data = json.loads(f.read())
    with open('comment.data', 'w') as f:
        new_data = {
            "num": len(all_data) + 1,
            "username": name,
            "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            "content": content
        }
        all_data.append(new_data)
        f.write(json.dumps(all_data))
    return json.dumps({"code": 200, "msg": "发表成功"})


if __name__ == '__main__':
    app.run(debug=True)
