from flask import Flask
from flask import json
from flask import request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/github',methods=['POST'])
def github_api():
    if request.headers['Content-Type']=='application/json':
        info = request.json
        print(info)
    return info
    


if __name__ == '__main__':
    app.run(debug=True)