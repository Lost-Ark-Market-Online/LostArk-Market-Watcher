import typing
import cv2
import numpy as np
import pytesseract
import os

from concurrent.futures import ThreadPoolExecutor, wait
from modules.common.market_line import MarketLine
from modules.common.point import Point
from modules.common.rect import Rect
from modules.market import filter_market_item_name, get_market_item_by_name
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
    'searchMarket': {
        'yMargin': 338,
        'yItemSpacing': 114,
        'itemHeight': 90,
        'xItemStops': [630, 1248, 1590, 1920, 2320],
        'xItemWidths': [500, 240, 220, 215, 330]
    },
    'baseRes': {
        'x': 3840,
        'y': 2160
    }
}


def get_text(screenshoot, rect: Rect, is_name: bool = False) -> str:
    """Detect Text inside rect within the screenshot"""

    # Crop image
    cropped_img = screenshoot[rect.y1:rect.y2, rect.x1:rect.x2]

    # Convert to Grayscale
    pimg = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

    # Scale Up cropped text to make detection easier for Tesseract
    pimg = cv2.resize(pimg, dsize=(
        int(pimg.shape[1]*3), int(pimg.shape[0]*3)))

    # Adjust image white levels for feature isolation
    pimg = cv2.addWeighted(pimg, 1.8, pimg, 0, -102)

    # Feature isolation: Detect black space and crop it
    coords = cv2.findNonZero(pimg)
    x, y, w, h = cv2.boundingRect(coords)
    if(w == 0 or h == 0):
        return None
    pimg = pimg[y:y+h, x:x+w]
    pimg = cv2.copyMakeBorder(
        pimg, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

    # Invert to White background and Black text
    pimg = cv2.bitwise_not(pimg)

    # Filter fuzziness
    _, pimg = cv2.threshold(pimg, 240, 255, cv2.THRESH_BINARY)

    # Sharpen borders
    element = cv2.getStructuringElement(
        shape=cv2.MORPH_RECT, ksize=(3, 3))
    pimg = cv2.erode(pimg, element, 3)

    # Process image into text using Tesseract
    e_text = ""
    if(is_name == True):
        e_text = pytesseract.image_to_string(
            pimg, lang='eng', config='--psm 6 -c tessedit_char_blacklist=!').strip()
    else:
        e_text = pytesseract.image_to_string(
            pimg, lang='eng', config='--psm 13 --oem 1 -c tessedit_char_whitelist=0123456789.').strip()

    return e_text


def get_rarity(screenshoot, rect: Rect) -> int:
    """
    Detect Rarity inside rect within the screenshot based on color
    - 0 = Normal
    - 1 = Uncommon
    - 2 = Rare
    - 3 = Epic
    - 4 = Legendary
    - 5 = Relic
    """

    # Crop image
    rarity_img = screenshoot[rect.y1:rect.y2, rect.x1:rect.x2]

    # Convert into Hue Saturation Vibrance
    rarity_img = cv2.cvtColor(rarity_img, cv2.COLOR_BGR2HSV)

    # Split values and keep Hue and Saturation
    rarity_img_h, rarity_img_s, _ = cv2.split(rarity_img)

    # Get value averages for Hue and for Saturation
    color_value = np.average(rarity_img_h)
    saturation_value = np.average(rarity_img_s)

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
        elif(color_value < 100):
            return 2
        elif(color_value < 150):
            return 3
        else:
            return 0


def process_line_column(screenshoot, tab, anchor, line_index, column_index) -> typing.Tuple[int, str | None] | (str | None):
    """Process column from a specific line"""
    # Build column starting point
    rect_start = Point(
        x=int(anchor.x + scanMap[tab]
              ['xItemStops'][column_index]),
        y=int(anchor.y + (scanMap[tab]['yMargin']) +
              line_index*scanMap[tab]['yItemSpacing'])
    )

    # Build rect to process
    rect = Rect(
        x1=rect_start.x,
        y1=rect_start.y,
        x2=int(rect_start.x +
               scanMap[tab]['xItemWidths'][column_index]),
        y2=int(rect_start.y + scanMap[tab]
               ['itemHeight'])
    )

    # If it is the first column, also detect rarity
    if column_index == 0:
        rarity = get_rarity(
            screenshoot, rect.add(-5, -5, 5, 5))
        item = get_text(
            screenshoot, rect, True)
        return rarity, item
    else:
        return get_text(
            screenshoot, rect)


def process_line(screenshoot, tab, anchor, line_index) -> MarketLine | None:
    """Process line columns using multithreading"""
    # Initialize executor and futures list
    column_futures = []
    executor = ThreadPoolExecutor(max_workers=5)

    # Push tasks and wait for them to finish
    for column_index in range(5):
        column_futures.append(executor.submit(
            process_line_column, screenshoot, tab, anchor, line_index, column_index))
    wait(column_futures)
    # Consolidate results
    columns = [column_future.result() for column_future in column_futures]

    # Item name cleanup
    name = columns[0][1]

    if name is None:
        return None

    if name.find('[Sold in bundles') > 0:
        name = name[0:name.find('[Sold in bundles')].strip()
    if name.find('[Untradable upon') > 0:
        name = name[0:name.find('[Untradable upon')].strip()

    # Filter name with whitelist
    name = filter_market_item_name(name)

    return MarketLine(
        rarity=columns[0][0],
        name=name,
        avg_price=process_number(columns[1]),
        recent_price=process_number(columns[2]),
        lowest_price=process_number(columns[3]),
        cheapest_remaining=process_number(columns[4])
    )


def process_market_table(screenshot, tab, anchor) -> typing.List[MarketLine]:
    """Process market table using multithreading"""
    # Initialize executor and futures list
    line_futures = []
    executor = ThreadPoolExecutor(max_workers=2)

    # Push tasks and wait for them to finish
    for line_index in range(10):
        line_futures.append(executor.submit(
            process_line, screenshot, tab, anchor, line_index))
    wait(line_futures)

    # Consolidate results
    return [line_future.result() for line_future in line_futures if line_future.result()]


def match_market(screenshoot, interest_tab=False) -> typing.Tuple[float, typing.Tuple[int, int]]:
    """Process market table using multithreading"""
    # Read Search Market tab sample
    sample = cv2.imread(os.path.abspath(os.path.join(
        os.path.dirname(__file__), '../assets/interest_market.jpg' if interest_tab == True else '../assets/search_market.jpg')))

    # Convert sample into Hue Saturation Vibrance
    sample = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)

    # Split sample and keep Vibrance
    _, _, sample_v = cv2.split(sample)

    # Convert screenshot into Hue Saturation Vibrance
    screenshoot_hsv = cv2.cvtColor(screenshoot, cv2.COLOR_BGR2HSV)

    # Split screenshot and keep Vibrance
    _, _, screenshoot_v = cv2.split(
        screenshoot_hsv)

    # Perform match template and keep the conficence value and location of the match
    res = cv2.matchTemplate(
        screenshoot_v, sample_v, cv2.TM_CCOEFF_NORMED)
    _, maxVal, _, maxLoc = cv2.minMaxLoc(res)

    return maxVal, maxLoc


def detect_market(screenshot) -> typing.Tuple[str, Point]:
    """Detect which market tab is open"""

    # Get confidence values for matching either search tab or interest tab
    interest_list_conf, interest_list_loc = match_market(screenshot, True)
    search_market_conf, search_market_loc = match_market(screenshot)

    loc = None
    tab = None

    # Pick the one with highest confidence
    if(interest_list_conf > search_market_conf):
        if(interest_list_conf > threshold):
            loc = interest_list_loc
            tab = 'interest'
        else:
            raise Exception('NO_MARKET')
    else:
        if(search_market_conf > threshold):
            loc = search_market_loc
            tab = 'searchMarket'
        else:
            raise Exception('NO_MARKET')

    return tab, Point(loc[0], loc[1])


def scan(filepath) -> typing.List[MarketLine]:
    """Scan market screenshot"""
    # Load screenshot
    screenshoot = cv2.imread(filepath)

    # Resize into measurements scale
    scale = {
        'x': screenshoot.shape[1] / scanMap['baseRes']['x'],
        'y': screenshoot.shape[0] / scanMap['baseRes']['y']
    }
    screenshoot = cv2.resize(screenshoot, dsize=(
        int(screenshoot.shape[1] / scale['x']), int(screenshoot.shape[0] / scale['y'])))

    # Detect which Market tab is open
    tab, anchor = detect_market(screenshoot)

    # Process market tab
    return process_market_table(screenshoot, tab, anchor)