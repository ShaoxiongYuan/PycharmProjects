from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/load')
def load():
    return render_template('demo01.html')


@app.route('/load_server', methods=['GET', 'POST'])
def load_server():
    # if request.method == 'GET':
    #     uname = request.args.get('uname')
    #     age = request.args.get('age')
    #     print(uname, age)
    # elif request.method == 'POST':
    #     uname = request.form.get('uname')
    #     age = request.form.get('age')
    #     print(uname, age)
    return render_template('demo01_server.html')


@app.route('/header')
def header_view():
    return render_template('header.html')


@app.route('/footer')
def footer_view():
    return render_template('footer.html')


if __name__ == '__main__':
    app.run(debug=True)
