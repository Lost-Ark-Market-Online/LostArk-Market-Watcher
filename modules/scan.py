from operator import itemgetter
from pathlib import Path
from shutil import rmtree
import typing
import cv2
from cv2 import log
import numpy as np
import pytesseract
import os
import re

from concurrent.futures import ThreadPoolExecutor, wait
from modules.common.market_line import MarketLine
from modules.common.point import Point
from modules.common.rect import Rect
from modules.config import Config
from modules.logging import AppLogger
from modules.market import filter_market_item_name
from modules.process import process_number

pytesseract.pytesseract.tesseract_cmd = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../lib/Tesseract-OCR/tesseract'))

threshold = .8

scanMap = {
    'interest': {
        'yMargin': 250,
        'yItemSpacing': 114,
        'itemHeight': 90,
        'xItemStops': [130, 1230, 1570, 1900, 2300],
        'xItemWidths': [700, 240, 220, 215, 330]
    },
    'market': {
        'yMargin': 338,
        'yItemSpacing': 114,
        'itemHeight': 90,
        'xItemStops': [630, 1248, 1590, 1920, 2320],
        'xItemWidths': [500, 240, 220, 215, 330]
    },
    'purchase_gold': {
        'x': 1300,
        'y': 210,
        'w': 165,
        'h': 70
    },
    'buy_crystals': {
        'x': 1300,
        'y': 210,
        'w': 165,
        'h': 70
    },
    'baseRes': {
        'x': 3840,
        'y': 2160
    }
}


class Scan():
    screenshot = None
    debug_screenshot = None
    debug_file = None
    tab: str
    anchor: Point
    result: typing.List[MarketLine]

    def __init__(self, filepath):
         
        if Config().debug:
            AppLogger().debug('Directories cleanup')
            self.debug_file = 'debug/' + Path(filepath).stem

            if os.path.isdir(f'{self.debug_file}'):
                rmtree(f'{self.debug_file}')

            os.mkdir(f'{self.debug_file}')
            os.mkdir(f'{self.debug_file}/inspection')
            
        self.screenshot = cv2.imread(filepath)
        self.debug_screenshot = self.screenshot.copy()

        if Config().debug:
            AppLogger().debug(f"file: {Path(filepath).stem}")
            cv2.imwrite(f'{self.debug_file}/1-screenshot.jpg', self.debug_screenshot)

        # Crop black borders
        self.crop_image()

        # Resize into measurements scale
        self.resize_screenshot()

        # Detect which Market tab is open
        self.detect_market()

        match self.tab:
            case "market":
                self.process_market_table()
            case "interest":
                self.process_market_table()
            case "buy_crystals":
                self.process_crystal_table()
            case "purchase_gold":
                self.process_crystal_table()
    
    def crop_image(self):
        """Remove black bars surrounding screenshot"""

        screenshot_middle = int(self.screenshot.shape[1] / 2)
        crop_detect_sc = self.screenshot[0:self.screenshot.shape[0],
                                    screenshot_middle-int(self.screenshot.shape[1]/4):screenshot_middle+int(self.screenshot.shape[1]/4)]

        if Config().debug:
            cv2.imwrite(f'{self.debug_file}/2.1-crop_detect_sc.jpg', crop_detect_sc)

        res = cv2.cvtColor(crop_detect_sc, cv2.COLOR_BGR2GRAY)
        res = cv2.addWeighted(res, 1.8, res, 0, -20)

        if Config().debug:
            cv2.imwrite(f'{self.debug_file}/2.2-crop_detect_sc_contrast.jpg', res)

        coords = cv2.findNonZero(res)
        x, y, w, h = cv2.boundingRect(coords)
        self.screenshot = self.screenshot[y:y+h, 0:self.screenshot.shape[1]]

        if Config().debug:
            self.debug_screenshot = self.screenshot.copy()
            cv2.imwrite(f'{self.debug_file}/2.3-cropped-screenshot.jpg', self.debug_screenshot)

    def resize_screenshot(self):
        """Standarize screenshot size for matching"""

        scale = {
            'x': self.screenshot.shape[1] / scanMap['baseRes']['x'],
            'y': self.screenshot.shape[0] / scanMap['baseRes']['y']
        }

        self.screenshot = cv2.resize(self.screenshot, dsize=(
            int(self.screenshot.shape[1] / scale['y']), int(self.screenshot.shape[0] / scale['y'])))

        if Config().debug:
            self.debug_screenshot = self.screenshot.copy()
            cv2.imwrite(f'{self.debug_file}/3-resized-screenshot.jpg', self.screenshot)

    def match_market(self, tab="market") -> typing.Tuple[float, typing.Tuple[int, int]]:
        """Process market table using multithreading"""
        # Read Search Market tab sample
        sample_file = ""
        match tab:
            case "market":
                sample_file = "../assets/search_market.jpg"
            case "interest":
                sample_file = "../assets/interest_market.jpg"
            case "purchase_gold":
                sample_file = "../assets/purchase_gold.jpg"
            case "buy_crystals":
                sample_file = "../assets/buy_crystals.jpg"
            case _:
                raise Exception("Invalid tab")

        sample = cv2.imread(os.path.abspath(os.path.join(
            os.path.dirname(__file__), sample_file)))

        # Convert sample into Hue Saturation Vibrance
        sample = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)

        # Split sample and keep Vibrance
        _, _, sample_v = cv2.split(sample)

        # Convert screenshot into Hue Saturation Vibrance
        screenshot_hsv = cv2.cvtColor(self.screenshot, cv2.COLOR_BGR2HSV)

        # Split screenshot and keep Vibrance
        _, _, screenshot_v = cv2.split(
            screenshot_hsv)

        # Perform match template and keep the conficence value and location of the match
        res = cv2.matchTemplate(
            screenshot_v, sample_v, cv2.TM_CCOEFF_NORMED)
        _, maxVal, _, maxLoc = cv2.minMaxLoc(res)

        if Config().debug == True:
            AppLogger().debug(f"{tab}: {maxVal}")
            if maxVal > threshold:
                self.debug_screenshot = cv2.rectangle(
                    self.debug_screenshot, (maxLoc[0], maxLoc[1]), (maxLoc[0]+sample.shape[1], maxLoc[1]+sample.shape[0]), (0, 0, 255), 2)
                AppLogger().debug(f"Found Market tab: {tab}")

        return maxVal, maxLoc, tab

    def detect_market(self) -> typing.Tuple[str, Point]:
        """Detect which market tab is open"""

        # Get confidence values for matching either search tab or interest tab
        matches = []
        matches.append(self.match_market("interest"))

        matches.append(self.match_market("market"))

        matches.append(self.match_market("buy_crystals"))

        matches.append(self.match_market("purchase_gold"))

        match_conf, loc, tab = max(matches, key=itemgetter(0))

        if(match_conf < threshold):
            raise Exception('NO_MARKET')

        self.tab = tab
        self.anchor = Point(loc[0], loc[1])

    def process_market_table(self) -> typing.List[MarketLine]:
        """Process market table using multithreading"""
        # Initialize executor and futures list
        line_futures = []
        executor = ThreadPoolExecutor(max_workers=Config().scan_threads)

        # Push tasks and wait for them to finish
        for line_index in range(10):
            line_futures.append(executor.submit(
                self.process_line, line_index))
        wait(line_futures)

        if Config().debug:
            cv2.imwrite(f'{self.debug_file}/4-processed-screenshot.jpg', self.debug_screenshot)

        # Consolidate results
        self.result = [line_future.result() for line_future in line_futures if line_future.result()]

    def process_crystal_table(self):
        rect_start = Point(
            x=int(self.anchor.x + scanMap[self.tab]['x']),
            y=int(self.anchor.y + (scanMap[self.tab]['y']))
        )
        rect = Rect(rect_start.x, rect_start.y,
                    rect_start.x + scanMap[self.tab]['w'], rect_start.y + scanMap[self.tab]['h'])

        price = int(self.get_text(rect, False).replace(".","").replace(",",""))

        if Config().debug:
            self.debug_screenshot = cv2.rectangle(
                self.debug_screenshot, (rect.x1, rect.y1), (rect.x2, rect.y2), (255, 255, 255), 1)
            cv2.imwrite(f'{self.debug_file}/4-processed-screenshot.jpg.jpg', self.screenshot)

        match self.tab:
            case "purchase_gold":
                name = "Royal Crystal"
                AppLogger().debug(f"Raw - {name}: {price}")
                price = round(price/238, 2)
            case "buy_crystals":
                name = "Blue Crystal"
                AppLogger().debug(f"Raw - {name}: {price}")
                price = round(price/95, 2)

        self.result = [MarketLine(0, name, price, price, price, 1)]

    def process_line(self, line_index) -> MarketLine | None:
        """Process line columns using multithreading"""
        # Initialize executor and futures list
        column_futures = []
        executor = ThreadPoolExecutor(max_workers=Config().scan_threads)

        # Push tasks and wait for them to finish
        for column_index in range(5):
            column_futures.append(executor.submit(
                self.process_line_column, line_index, column_index))
        wait(column_futures)

        # Consolidate results
        columns = [column_future.result() for column_future in column_futures]

        # Item name cleanup
        name = columns[0][1]

        if name is None:
            return None


        name = re.sub(f"\n.*S[oa][il]d in bund[il]es.*", "", name)

        name = re.sub(f"\n.*Untradable upon.*", "", name)

        AppLogger().info(f"Scanned Name: {name}")

        # Filter name with whitelist
        name = filter_market_item_name(name)

        AppLogger().info(f"Filtered Name: {name}")

        return MarketLine(
            rarity=columns[0][0],
            name=name,
            avg_price=process_number(columns[1]),
            recent_price=process_number(columns[2]),
            lowest_price=process_number(columns[3]),
            cheapest_remaining=process_number(columns[4])
        )

    def process_line_column(self, line_index, column_index) -> typing.Tuple[int, str | None] | (str | None):
        """Process column from a specific line"""
        # Build column starting point
        rect_start = Point(
            x=int(self.anchor.x + scanMap[self.tab]
                ['xItemStops'][column_index]),
            y=int(self.anchor.y + (scanMap[self.tab]['yMargin']) +
                line_index*scanMap[self.tab]['yItemSpacing'])
        )

        # Build rect to process
        rect = Rect(
            x1=rect_start.x,
            y1=rect_start.y,
            x2=int(rect_start.x +
                scanMap[self.tab]['xItemWidths'][column_index]),
            y2=int(rect_start.y + scanMap[self.tab]
                ['itemHeight'])
        )

        # If it is the first column, also detect rarity
        if column_index == 0:
            item = self.get_text(rect, True)
            rarity = self.get_rarity(rect)
            return rarity, item
        else:
            return self.get_text(rect, False)

    def get_text(self, rect: Rect, is_name: bool = False) -> str:
        """Detect Text inside rect within the screenshot"""

        # Crop image
        cropped_img = self.screenshot[rect.y1:rect.y2, rect.x1:rect.x2]

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-1-cropped.jpg', cropped_img)

        # Convert to Grayscale
        pimg = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-2-gray.jpg', pimg)

        # Scale Up cropped text to make detection easier for Tesseract
        pimg = cv2.resize(pimg, dsize=(
            int(pimg.shape[1]*3), int(pimg.shape[0]*3)))

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-3-scaled.jpg', pimg)

        # Adjust image white levels for feature isolation
        pimg = cv2.addWeighted(pimg, 1.65, pimg, 0, -120)

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-4-contrast.jpg', pimg)

        # Feature isolation: Detect black space and crop it
        coords = cv2.findNonZero(pimg)
        x, y, w, h = cv2.boundingRect(coords)
        if(w == 0 or h == 0):
            return None
        pimg = pimg[y:y+h, x:x+w]
        pimg = cv2.copyMakeBorder(
            pimg, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-5-isolated.jpg', pimg)

        # Invert to White background and Black text
        pimg = cv2.bitwise_not(pimg)

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-6-flipped.jpg', pimg)

        # Filter fuzziness
        _, pimg = cv2.threshold(pimg, 240, 255, cv2.THRESH_BINARY)

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-7-filtered.jpg', pimg)

        # Sharpen borders
        element = cv2.getStructuringElement(
            shape=cv2.MORPH_RECT, ksize=(3, 3))
        pimg = cv2.erode(pimg, element, 3)

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-8-sharpen.jpg', pimg)

        # Process image into text using Tesseract
        e_text = ""
        if(is_name == True):
            e_text = pytesseract.image_to_string(
                pimg, lang='eng', config='--psm 6 -c tessedit_char_blacklist=!').strip()
        else:
            e_text = pytesseract.image_to_string(
                pimg, lang='eng', config='--psm 13 --oem 1 -c tessedit_char_whitelist=0123456789.').strip()

        if Config().debug:
            AppLogger().debug(f"Text Scan: {e_text}")
            self.debug_screenshot = cv2.rectangle(
                self.debug_screenshot, (rect.x1, rect.y1), (rect.x2, rect.y2), (0, 255, 255), 2)
        return e_text

    def get_rarity(self, rect: Rect) -> int:
        """
        Detect Rarity inside rect within the screenshot based on color
        - 0 = Normal
        - 1 = Uncommon
        - 2 = Rare
        - 3 = Epic
        - 4 = Legendary
        - 5 = Relic
        - 6 = Ancient
        - 7 = Sidereal
        """
        # Get sample rect from the bottom left corner
        sample_rect = Rect(rect.x1, rect.y2, rect.x1, rect.y2).add(-5, -5, 5, 5)

        # Crop image
        rarity_img = self.screenshot[sample_rect.y1:sample_rect.y2,
                                sample_rect.x1:sample_rect.x2]

        if Config().debug:
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-9-rarity-sample.jpg', rarity_img)

        # Convert into Hue Saturation Vibrance
        rarity_img = cv2.cvtColor(rarity_img, cv2.COLOR_BGR2HSV)

        # Split values and keep Hue and Saturation
        rarity_img_h, rarity_img_s, _ = cv2.split(rarity_img)

        # Get value averages for Hue and for Saturation
        color_value = np.average(rarity_img_h)
        saturation_value = np.average(rarity_img_s)

        if Config().debug:
            AppLogger().debug(f"Rarity Scan {rect.y1}-{rect.x1}: color_value({color_value})")
            AppLogger().debug(f"Rarity Scan {rect.y1}-{rect.x1}: saturation_value({color_value})")
            self.debug_screenshot = cv2.rectangle(
                self.debug_screenshot, (sample_rect.x1, sample_rect.y1), (sample_rect.x2, sample_rect.y2), (255, 255, 255), 1)
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-9-rarity-hue.jpg', rarity_img_h)
            cv2.imwrite(
                f'{self.debug_file}/inspection/text-{rect.y1}-{rect.x1}-9-rarity-saturation.jpg', rarity_img_s)


        # Classify rarity by the Hue and Saturation
        if(saturation_value < 50):
            return 0
        else:
            if(color_value < 15):
                return 5
            elif(color_value < 20):
                return 4
            elif(color_value < 50):
                return 1
            elif(color_value < 89):
                return 7
            elif(color_value < 100):
                return 2
            elif(color_value < 150):
                return 3
            else:
                return 0

def scan_file(file):
    scan = Scan(file)
    return scan.result