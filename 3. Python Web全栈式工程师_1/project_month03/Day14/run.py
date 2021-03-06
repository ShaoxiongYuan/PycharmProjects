from flask import Flask, render_template

app = Flask(__name__)


@app.route('/demo')
def demo_view():
    return render_template('demo01.html')


@app.route('/')
def index_view():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
