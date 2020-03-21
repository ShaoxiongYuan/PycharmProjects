from flask import Flask, render_template, request
import json

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
