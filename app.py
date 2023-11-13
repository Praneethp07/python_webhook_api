from flask import Flask
from flask import json
from flask import request
import subprocess

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/github',methods=['POST'])
def github_api():
    if request.headers['Content-Type']=='application/json':
        info = request.json
        print(info)
        pull_command = "cd ~/Chat_Api && git pull origin main"
        restart_pm2_command = "pm2 restart server.js"
        restart_nginx_command = "sudo systemctl restart nginx"
        print_output = "echo 'Application deployed successfully'"
        subprocess.run(pull_command, shell=True)
        subprocess.run(restart_pm2_command, shell=True)
        subprocess.run(restart_nginx_command, shell=True)
        subprocess.run(print_output,shell=True)
    return info
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)