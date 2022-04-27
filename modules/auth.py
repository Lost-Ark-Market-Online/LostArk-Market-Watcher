import requests
from modules.config import update_token
from modules.errors import NoTokenError

api_key = 'AIzaSyBMTA0A2fy-dh4jWidbAtYseC7ZZssnsmk'


def refresh_token(token):
    res = requests.post(f'https://securetoken.googleapis.com/v1/token?key={api_key}', json={
        'refresh_token': token,
        'grant_type': 'refresh_token'
    })
    tokens = res.json()
    if 'error' in tokens:
        raise NoTokenError()
    update_token({
        "id_token": tokens['id_token'],
        "refresh_token": tokens['refresh_token'],
        "uid": tokens['user_id'],
    })
    return tokens['id_token'], tokens['refresh_token'], tokens['user_id']
