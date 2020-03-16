from flask import Flask

app = Flask(__name__)


@app.route('/easy')
def easy():
    return '低级难度'


@app.route('/middle')
def middle():
    return '中级难度'


@app.route('/high')
def high():
    return '高级难度'


if __name__ == '__main__':
    app.run(debug=True)
