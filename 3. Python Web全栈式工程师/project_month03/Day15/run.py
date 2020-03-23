import json

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
    return json.dumps({"code": 200, "data": data})


if __name__ == '__main__':
    app.run(debug=True)
