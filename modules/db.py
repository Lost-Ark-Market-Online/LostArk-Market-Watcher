
import traceback
from datetime import datetime, timedelta
from slugify import slugify
from google.oauth2.credentials import Credentials
from google.cloud.firestore import Client
from modules.auth import refresh_token
from modules.common.market_line import MarketLine
from modules.config import get_tokens
from modules.errors import NoTokenError
from modules.market import get_market_item_by_name
from modules.process import process_item
from modules.sound import playError, playPulse
from PySide6.QtCore import Signal, QObject

project = 'lostarkmarket-79ddf'


class MarketDb(QObject):
    log: Signal = Signal(str)
    error: Signal = Signal(str)
    region: str = None
    id_token: str = None
    refresh_token: str = None
    uid: str = None
    creds: Credentials = None
    db: Client = None
    last_refresh: datetime = None
    version: str = None

    def __init__(self, version):
        try:
            super(MarketDb, self).__init__()
            self.refresh_credentials()
            self.version = version
            self.db = Client(project=project, credentials=self.creds)
            self.region = self.db.document(
                f'collaborators/{self.uid}').get().get('region')
        except NoTokenError:
            traceback.print_exc()

    def refresh_credentials(self):
        needs_refresh = False
        if self.last_refresh is None:
            needs_refresh = True
        elif self.last_refresh + timedelta(minutes=30) < datetime.now():
            needs_refresh = True
        
        if needs_refresh:
            self.log.emit(f"Refresh credentials")
            try:            
                if self.refresh_token is None:            
                    _, self.refresh_token, _ = get_tokens()
                self.id_token, self.refresh_token, self.uid = refresh_token(
                    self.refresh_token)
                self.creds = Credentials(
                    token=self.id_token,
                    refresh_token=self.refresh_token
                )
                self.last_refresh = datetime.now()
            except:
                self.error.emit("Error getting credentials")
                self.error.emit(traceback.format_exc)


    def add_entry(self, market_line: MarketLine, play_audio=True):
        try:
            # Refresh credentials if needed
            self.refresh_credentials()

            # Get item data based on dictionary
            item = process_item(market_line)

            # Update rarity based on market dictionary
            market_line.rarity = item['rarity']

            # Get Doc
            item_doc_ref = self.db.document(
                f"{self.region}/{slugify(item['name'])}-{market_line.rarity}")
            item_doc = item_doc_ref.get()

            if (
                market_line.lowest_price == None or 
                market_line.recent_price == None or 
                market_line.cheapest_remaining == None
            ):
                raise Exception('NO_VALID_PRICE_FOUND')

            if (item_doc.exists == False):
                self.log.emit(
                    f"Create {self.region}/{slugify(item['name'])}-{market_line.rarity}")

                item['updatedAt'] = datetime.utcnow()
                item_doc_ref.create(item)
            else:
                to_update = {}
                if market_line.avg_price:
                    to_update['avgPrice'] = market_line.avg_price
                else:
                    to_update['avgPrice'] = market_line.lowest_price
                
                to_update['cheapestRemaining'] = market_line.cheapest_remaining            
                to_update['lowPrice'] = market_line.lowest_price            
                to_update['recentPrice'] = market_line.recent_price                
                to_update['updatedAt'] = datetime.utcnow()
                to_update['author'] = self.uid
                to_update['watcher_version'] = self.version

                item_doc_ref.update(to_update)

            item_doc_ref.collection('entries').add({
                'avgPrice': market_line.avg_price,
                'cheapestRemaining': market_line.cheapest_remaining,
                'lowPrice': market_line.lowest_price,
                'recentPrice': market_line.recent_price,
                'createdAt': datetime.utcnow(),
                'author': self.uid,
                'watcher_version': self.version
            })

            self.log.emit(f"Updated: {market_line.name} | {market_line.avg_price} | {market_line.recent_price} | {market_line.lowest_price} | {market_line.cheapest_remaining}")
            if play_audio == True:
                playPulse()
        except:
            self.error.emit(f"Failed: {market_line.name} | {market_line.avg_price} | {market_line.recent_price} | {market_line.lowest_price} | {market_line.cheapest_remaining}")
            self.error.emit(traceback.format_exc())
            if play_audio == True:
                playError()
