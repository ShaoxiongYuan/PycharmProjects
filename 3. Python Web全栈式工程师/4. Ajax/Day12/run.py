from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/post', methods=['GET', 'POST'])
def view1():
    if request.method == 'GET':
        return render_template('demo01.html')
    elif request.method == 'POST':
        uname = request.form.get('uname')
        return '欢迎%s' % uname


if __name__ == '__main__':
    app.run(debug=True)
