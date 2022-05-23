
import traceback
from datetime import datetime, timedelta
from cv2 import trace
from slugify import slugify
from google.oauth2.credentials import Credentials
from google.cloud.firestore import Client
from modules.auth import refresh_token
from modules.common.market_line import MarketLine
from modules.config import Config
from modules.errors import NoTokenError
from modules.logging import AppLogger
from modules.process import process_item
from modules.sound import playError, playPulse
from PySide6.QtCore import Signal, QObject
from packaging import version
from google.api_core.exceptions import Unauthenticated

project = 'lostarkmarket-79ddf'


class MarketDb(QObject):
    new_version: Signal = Signal(str)
    creds: Credentials = None
    db: Client = None
    last_refresh: datetime = None

    def __init__(self):
        try:
            super(MarketDb, self).__init__()
            self.refresh_credentials()
            self.db = Client(project=project, credentials=self.creds)
            Config().region = self.db.document(
                f'collaborators/{Config().uid}').get().get('region')
            AppLogger().info(f"Got Watcher Region: '{Config().region}'")
            self.db.document(
                "app-info/market-watcher").on_snapshot(self.new_version_cb)
        except NoTokenError as ex:
            AppLogger().exception(ex)

    def refresh_credentials(self, forced=False):
        if (self.last_refresh is None) or (self.last_refresh + timedelta(minutes=30) < datetime.now()) or forced:
            AppLogger().info(f"Refresh credentials")
            try:
                refresh_token()
                self.creds = Credentials(
                    token=Config().id_token,
                    refresh_token=Config().refresh_token
                )
                self.last_refresh = datetime.now()
            except Exception as ex:
                AppLogger().exception(ex)

    def add_entry(self, market_line: MarketLine, retries: int = 0):
        try:
            # Refresh credentials if needed
            self.refresh_credentials()

            # Get item data based on dictionary
            item = process_item(market_line)

            # Update rarity based on market dictionary
            market_line.rarity = item['rarity']

            # Get Doc
            item_doc_ref = self.db.document(
                f"{Config().region}/{slugify(item['name'])}-{market_line.rarity}")
            item_doc = item_doc_ref.get()

            if (
                market_line.lowest_price == None or
                market_line.recent_price == None or
                market_line.cheapest_remaining == None
            ):
                raise Exception('NO_VALID_PRICE_FOUND')

            if (item_doc.exists == False):
                AppLogger().info(
                    f"Create {Config().region}/{slugify(item['name'])}-{market_line.rarity}")

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
                to_update['author'] = Config().uid
                to_update['watcher_version'] = Config().version

                item_doc_ref.update(to_update)

            item_doc_ref.collection('entries').add({
                'avgPrice': market_line.avg_price,
                'cheapestRemaining': market_line.cheapest_remaining,
                'lowPrice': market_line.lowest_price,
                'recentPrice': market_line.recent_price,
                'createdAt': datetime.utcnow(),
                'author': Config().uid,
                'watcher_version': Config().version
            })
            AppLogger().info(
                f"Updated: {market_line.name} | {market_line.avg_price} | {market_line.recent_price} | {market_line.lowest_price} | {market_line.cheapest_remaining}")
            if Config().play_audio:
                playPulse()
        except Unauthenticated:
            self.refresh_credentials(True)
            if retries < 3:
                self.add_entry(market_line, retries + 1)

        except Exception as ex:
            AppLogger().error(
                f"Failed: {market_line.name} | {market_line.avg_price} | {market_line.recent_price} | {market_line.lowest_price} | {market_line.cheapest_remaining}")
            AppLogger().exception(ex)
            if Config().play_audio:
                playError()

    def new_version_cb(self, snapshot, changes, read_time):
        for doc in snapshot:
            new_version = doc.get("version")
            if(version.parse(Config().version) < version.parse(new_version)):
                self.new_version.emit(new_version)
