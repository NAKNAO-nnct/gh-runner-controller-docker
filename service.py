import random
import config
import client

def run_container(client: client.DockerAPIClient, id = None):
    if id is not None:
        id = str(id)
    else:
        id = str(random.randint(0, 10000))

    environment = {
        'RUNNER_SCOPE': config.GITHUB_RUNNER_SCOPE,
        'ORG_NAME': config.GITHUB_ORG_NAME,
        'ACCESS_TOKEN': config.GITHUB_ACCESS_TOKEN,
        'EPHEMERAL': 'true',
        'DISABLE_AUTO_UPDATE': 'true',
    }

    volumes = [
        '/var/run/docker.sock:/var/run/docker.sock',
        '/root/.ssh:/root/.ssh',
    ]

    container_name = 'gha-runner-' + id

    print('container name: ', container_name)

    container = client.create_container(config.RUNNER_IMAGE, container_name, environment, volumes)

    print('container id: ', container.id)

def pull_image(client: client.DockerAPIClient):
    client.pull_image(config.RUNNER_IMAGE)
