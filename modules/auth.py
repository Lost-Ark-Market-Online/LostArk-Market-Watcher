import requests
from modules.config import Config
from modules.errors import NoTokenError

api_key = 'AIzaSyBMTA0A2fy-dh4jWidbAtYseC7ZZssnsmk'


def refresh_token():
    res = requests.post(f'https://securetoken.googleapis.com/v1/token?key={api_key}', json={
        'refresh_token': Config().refresh_token,
        'grant_type': 'refresh_token'
    })
    tokens = res.json()
    if 'error' in tokens:
        raise NoTokenError()
    Config().update_token({
        "id_token": tokens['id_token'],
        "refresh_token": tokens['refresh_token'],
        "uid": tokens['user_id'],
    })
