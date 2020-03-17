from flask import Flask, request

app = Flask(__name__)


@app.route('/test')
def test():
    level = request.args.get('level')
    if level == 'all':
        return '全部难度'
    elif level == 'easy':
        return '低级难度'
    elif level == 'middle':
        return '中级难度'
    elif level == 'high':
        return '高级难度'
    else:
        return '获取难度失败'


if __name__ == '__main__':
    app.run(debug=True)
