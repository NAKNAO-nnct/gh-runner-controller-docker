import dotenv
import os

dotenv.load_dotenv()

def get_env(key, default):
    value = os.environ.get(key)
    if value is None:
        return default
    return value

DOCKER_HOST_URL = get_env('DOCKER_HOST_URL', 'unix:///var/run/docker.sock')

APP_HOST = get_env('APP_HOST', '0.0.0.0')
APP_PORT = int(get_env('APP_PORT', '8080'))

GITHUB_RUNNER_SCOPE = get_env('GITHUB_RUNNER_SCOPE', 'repo')
GITHUB_ORG_NAME = get_env('GITHUB_ORG_NAME', 'example')
GITHUB_ACCESS_TOKEN = get_env('GITHUB_ACCESS_TOKEN', 'xxxxxxxx')
