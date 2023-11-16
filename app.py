from flask import Flask, json, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/github', methods=['POST'])
def github_api():
    if request.headers['Content-Type'] == 'application/json':
        info = request.json
        # print(info)

        # Fetch the latest changes from the remote repository
        fetch_command = "cd ~/Chat_Api && git fetch origin main"
        subprocess.run(fetch_command, shell=True)

        # Reset local branch to match the remote branch
        reset_command = "cd ~/Chat_Api && git reset --hard origin/main"
        subprocess.run(reset_command, shell=True)

        # Clean any untracked files and directories
        clean_command = "cd ~/Chat_Api && git clean -df && npm install express && npm install"
        subprocess.run(clean_command, shell=True)

        # Restart PM2-managed server
        restart_pm2_command = "pm2 reload server"
        subprocess.run(restart_pm2_command, shell=True)

        # Restart Nginx
        restart_nginx_command = "cd && sudo systemctl restart nginx"
        subprocess.run(restart_nginx_command, shell=True)

        print_output = "echo 'Application deployed successfully'"
        subprocess.run(print_output, shell=True)

    return info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

