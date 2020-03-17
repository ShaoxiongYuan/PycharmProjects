from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/region')
def choose_region():
    return render_template('exercise01.html')


@app.route('/server', methods=['POST'])
def server():
    uname = request.form.get('uname', '')
    return "欢迎%s" % uname


if __name__ == '__main__':
    app.run(debug=True)
