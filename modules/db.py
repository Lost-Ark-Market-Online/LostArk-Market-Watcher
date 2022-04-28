
import traceback
from datetime import datetime
from google.oauth2.credentials import Credentials
from google.cloud.firestore import Client
from modules.auth import refresh_token
from modules.common.market_line import MarketLine
from modules.config import get_tokens
from modules.errors import NoTokenError
from modules.market import get_market_item_by_name
from modules.sound import playPulse

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

    def add_entry(self, market_line: MarketLine, play_audio=True):
        try:
            item_doc = self.db.collection(self.region).where(
                'name', '==', market_line.name).where('rarity', '==', market_line.rarity).get()

            if(len(item_doc) == 0):
                item = get_market_item_by_name(market_line.name)
                item['updatedAt'] = datetime.utcnow()
                _, item_doc = self.db.collection(
                    self.region).add(document_data={**market_line.to_json(), **item})
            else:
                item_doc = item_doc[0]
                self.db.collection(self.region).document(item_doc.id).update({
                    'avgPrice': market_line.avg_price,
                    'cheapestRemaining': market_line.cheapest_remaining,
                    'lowPrice': market_line.lowest_price,
                    'recentPrice': market_line.recent_price,
                    'updatedAt': datetime.utcnow()
                })

            self.db.collection(self.region).document(item_doc.id).collection('entries').add({
                'avgPrice': market_line.avg_price,
                'cheapestRemaining': market_line.cheapest_remaining,
                'lowPrice': market_line.lowest_price,
                'recentPrice': market_line.recent_price,
                'createdAt': datetime.utcnow()
            })

            print(f"== Updated: {market_line.name} ==")
            if play_audio == True:
                playPulse()
        except:
            print(f"== Add Entry Failed: {market_line.name} ==")
            traceback.print_exc()
