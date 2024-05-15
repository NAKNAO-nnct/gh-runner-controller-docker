from flask import Flask, request
import threading

import config
import client
import service

app = Flask(__name__)

client = client.DockerAPIClient()

@app.route(config.APP_WEBHOOK_ENDPOINT, methods=['POST'])
def webhook():
    # request header から X-GitHub-Event を取得
    event = request.headers.get('X-GitHub-Event')
    hook_id = request.headers.get('X-GitHub-Delivery')
    print('x-github-hook-id: ', hook_id)
    print('x-github-event: ', event)

    if event == 'workflow_job':
        print('workflow_job')
        payload = request.json

        if payload['action'] == 'queued':
            thread = threading.Thread(target=service.run_container(client, hook_id))
            thread.start()
        elif payload['action'] == 'completed':
            print('completed')

    return {
        'status': 'ok'
    }

if __name__ == '__main__':
    app.run(host=config.APP_HOST, port=config.APP_PORT)
