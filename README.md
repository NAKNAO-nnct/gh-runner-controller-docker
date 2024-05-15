# GitHub Actions Self-Hosted Runner Controller with Docker

This project is a controller for GitHub Actions Self-Hosted Runner. While the official version only supports Kubernetes (k8s), we have created a simplified version that only uses Docker.

## Features
* Easy to set up and use
* Lightweight, only requires Docker
* Can be used on any system that supports Docker

## Setup
1. Install Docker on your system.
1. Clone this repository.
2. Create and Edit .env file
3. docker compose up -d
4. Register Webhook  
After starting the controller, you need to register the endpoint as a webhook in GitHub. If you are unable to access it globally, it is recommended to use Cloudflare Tunnel, ngrok, or similar services for exposing your local development server to the internet.

## Usage
Once the Docker container is running, it will automatically start controlling the GitHub Actions Self-Hosted Runner.

## Contribution
Contributions to this project are welcome. Please open an issue or pull request.

## License
This project is licensed under the MIT License.
