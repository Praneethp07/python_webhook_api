from flask import Flask
from flask import json
from flask import request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)