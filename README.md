# Chat API Deployment Automation

This repository contains a Flask application designed to automate the deployment of a Chat API. The application exposes two endpoints: `/` for a simple "hello" response and `/github` for handling GitHub webhooks to automate the deployment process.

## Prerequisites

Before using this deployment automation script, ensure you have the following dependencies installed:

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Node.js](https://nodejs.org/en/) (for npm packages installation)
- [PM2](https://pm2.keymetrics.io/) (for managing Node.js processes)
- [Nginx](https://www.nginx.com/) (for serving the API and handling reverse proxy)

## Installation

1. Clone the repository to your server:

   ```bash
   git clone <repository_url>
   cd Chat_Api

    Install the required Python and Node.js dependencies:

    bash

npm install express
npm install

Run the Flask application:

bash

    python app.py

    The application will run on http://0.0.0.0:5001/ by default.

GitHub Webhook Integration

To automate the deployment process, set up a GitHub webhook to send push events to the /github endpoint of your deployed application. Configure the webhook to send JSON payloads.
Deployment

The /github endpoint is designed to handle GitHub webhook events. When a push event occurs, the application performs the following steps:

    Fetch the latest changes from the remote repository.
    Reset the local branch to match the remote branch.
    Clean any untracked files and directories, and install Node.js dependencies.
    Restart the PM2-managed server.
    Restart Nginx.

Ensure that your server environment has the necessary permissions for these actions.
Customization

Feel free to customize the deployment script (app.py) based on your specific requirements. Update the commands in the /github route to match your project structure or additional deployment steps.
License

This project is licensed under the MIT License - see the LICENSE file for details.

csharp


Replace `<repository_url>` with the actual URL of your Git repository. Additionally, update the license section based on the license you choose for your project.

