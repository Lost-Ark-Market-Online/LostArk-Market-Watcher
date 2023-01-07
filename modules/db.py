
from concurrent.futures import ThreadPoolExecutor, wait
import traceback
from datetime import datetime, timedelta
import typing
from cv2 import trace
from slugify import slugify
from google.oauth2.credentials import Credentials
from google.cloud.firestore import Client
from modules.auth import Auth
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
    entry_futures = []
    entries_executor = ThreadPoolExecutor(
        max_workers=Config().upload_threads)

    def __init__(self):
        try:
            super(MarketDb, self).__init__()
            Auth().refresh_token()
            self.refresh_credentials(True)
            self.db = Client(project=project, credentials=self.creds)
            Config().region = self.db.document(
                f'collaborators/{Config().uid}').get().get('region')
            AppLogger().info(f"Got Watcher Region: '{Config().region}'")
            self.db.document(
                "app-info/market-watcher").on_snapshot(self.new_version_cb)
        except NoTokenError as ex:
            AppLogger().exception(ex)
            AppLogger().client.capture_exceptions()

    def refresh_credentials(self, forced=False):
        if (Auth().last_refresh + timedelta(minutes=30) < datetime.now()) or forced:
            AppLogger().info(f"Refresh credentials")
            try:
                Auth().refresh_token()
                self.creds = Credentials(
                    token=Config().id_token,
                    refresh_token=Config().refresh_token
                )
            except Exception as ex:
                AppLogger().exception(ex)
                AppLogger().client.capture_exceptions()

    def add_entries(self, market_lines: typing.List[MarketLine]):
        entry_futures = [self.entries_executor.submit(
                self.add_entry, item) for item in market_lines]        
        wait(entry_futures)

    def add_entry(self, market_line: MarketLine, retries: int = 0):
        try:
            with Auth().lock:
                # Refresh credentials if needed
                self.refresh_credentials()

                # Get item data based on dictionary
                item = process_item(market_line)

                # Update rarity based on market dictionary
                market_line.rarity = item['rarity']

                # Fill info if missing
                if market_line.recent_price is None:
                    market_line.recent_price = market_line.lowest_price
                if market_line.avg_price is None:
                    market_line.avg_price = market_line.lowest_price

                # Get Doc
                item_doc_ref = self.db.document(
                    f"{Config().region}/{slugify(item['name'])}-{market_line.rarity}")
                item_doc = item_doc_ref.get()

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
        except Unauthenticated as ex:
            self.refresh_credentials(True)
            if retries < 3:
                self.add_entry(market_line, retries + 1)
            else:
                AppLogger().client.capture_exceptions()
                raise Exception("Can't Authenticate - Please restart the App")
        except Exception as ex:
            AppLogger().error(
                f"Failed: {market_line.name} | {market_line.avg_price} | {market_line.recent_price} | {market_line.lowest_price} | {market_line.cheapest_remaining}")
            AppLogger().exception(ex)
            AppLogger().client.capture_exceptions()
            if Config().play_audio:
                playError()

    def new_version_cb(self, snapshot, changes, read_time):
        for doc in snapshot:
            new_version = doc.get("version")
            if(version.parse(Config().version) < version.parse(new_version)):
                self.new_version.emit(new_version)
