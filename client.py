import docker
import time
import random

import config

class DockerAPIClient:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DockerAPIClient, cls).__new__(cls)
            cls.instance.init()

        return cls.instance

    def init(self):
        self.client = docker.DockerClient(base_url=config.DOCKER_HOST_URL)

    def get_containers(self, is_all=False, filters={}):
        return self.client.containers.list(all=is_all, filters=filters)

    # コンテナ作成
    def create_container(self, image, name=None, environment={}, volumes=[]):
        print('create_container: ', name)
        return self.client.containers.run(
            image,
            detach=True,
            environment=environment,
            name=name,
            remove=True,
            volumes=volumes,
        )
