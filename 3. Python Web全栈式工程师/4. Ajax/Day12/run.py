from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/post')
def view1():
    return render_template('demo01.html')


@app.route('/post_server', methods=['POST'])
def server1():
    uname = request.form.get('uname')
    return '欢迎%s' % uname


if __name__ == '__main__':
    app.run(debug=True)
