
from datetime import datetime
from google.oauth2.credentials import Credentials
from google.cloud.firestore import Client

import requests
import json
import easygui
import os

from modules.market import get_market_item_by_name

api_key = 'AIzaSyBMTA0A2fy-dh4jWidbAtYseC7ZZssnsmk'
project = 'lostarkmarket-79ddf'


class MarketDb:
    region = None
    creds = None
    db = None

    def login(self):
        user, password = easygui.multpasswordbox(
            'Enter your Watcher account', 'Login', ['email', 'password'])
        tokens = self.login_request(user, password)
        self.creds = Credentials(
            token=tokens['idToken'],
            refresh_token=tokens['refreshToken']
        )
        self.db = Client(project=project, credentials=self.creds)
        with open('token.json', 'w') as token:
            token.write(self.creds.to_json())

    def login_request(self, user, password):
        res = requests.post(f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}', json={
            'email': user,
            'password': password,
            'returnSecureToken': True
        })
        return res.json()

    def refresh_token(self):
        res = requests.post(f'https://securetoken.googleapis.com/v1/token?key={api_key}', json={
            'refresh_token': self.creds.refresh_token,
            'grant_type': 'refresh_token'
        })
        tokens = res.json()
        self.creds = Credentials(
            token=tokens['id_token'],
            refresh_token=tokens['refresh_token']
        )
        self.db = Client(project=project, credentials=self.creds)
        with open('token.json', 'w') as token:
            token.write(self.creds.to_json())

    def __init__(self, region):
        self.region = region

        if os.path.exists('token.json'):
            with open('token.json') as token:
                token_dict = json.load(token)
                self.creds = Credentials(
                    token=token_dict['token'],
                    refresh_token=token_dict['refresh_token']
                )
                self.refresh_token()
        else:
            self.login()

    def add_entry(self, item):
        item_doc = self.db.collection(self.region).where(
            'name', '==', item['name']).get()

        if(len(item_doc) == 0):
            _, item_doc = self.db.collection(
                self.region).add(document_data=item)
        else:
            item_doc = item_doc[0]
            self.db.collection(self.region).document(item_doc.id).update({
                'avgPrice': item['avgPrice'],
                'cheapestRemaining': item['cheapestRemaining'],
                'lowPrice': item['lowPrice'],
                'recentPrice': item['recentPrice'],
                'updatedAt': datetime.utcnow()
            })

        self.db.collection(self.region).document(item_doc.id).collection('entries').add({
            'avgPrice': item['avgPrice'],
            'cheapestRemaining': item['cheapestRemaining'],
            'lowPrice': item['lowPrice'],
            'recentPrice': item['recentPrice'],
            'createdAt': datetime.utcnow()
        })
