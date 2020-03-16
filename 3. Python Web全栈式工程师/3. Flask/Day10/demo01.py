from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    视图函数
    :return: HTML
    """
    return "<h1>this is my first flask app</h1>"


@app.route('/show/<name>')
def show(name):
    return '<h1>你好' + name + '</h1>'


if __name__ == '__main__':
    app.run(debug=True)
