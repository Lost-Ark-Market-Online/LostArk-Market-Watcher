
import traceback
from datetime import datetime
from google.oauth2.credentials import Credentials
from google.cloud.firestore import Client
from modules.auth import refresh_token
from modules.config import get_tokens
from modules.errors import NoTokenError

project = 'lostarkmarket-79ddf'


class MarketDb:
    region = None
    creds = None
    db = None
    uid = None

    def __init__(self):
        try:
            _, self.refresh_token, _ = get_tokens()
            self.id_token, self.refresh_token, self.uid = refresh_token(
                self.refresh_token)
            self.creds = Credentials(
                token=self.id_token,
                refresh_token=self.refresh_token
            )
            self.db = Client(project=project, credentials=self.creds)
            self.region = self.db.document(
                f'collaborators/{self.uid}').get().get('region')
        except NoTokenError:
            traceback.print_exc()

    def add_entry(self, item):
        item_doc = self.db.collection(self.region).where(
            'name', '==', item['name']).where('rarity', '==', item['rarity']).get()

        if(len(item_doc) == 0):
            item['updatedAt'] = datetime.utcnow()
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
