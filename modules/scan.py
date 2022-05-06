from operator import itemgetter
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


def get_text(screenshot, rect: Rect, is_name: bool = False, debug: bool = False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> str:
    """Detect Text inside rect within the screenshot"""

    # Crop image
    cropped_img = screenshot[rect.y1:rect.y2, rect.x1:rect.x2]

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-1-cropped.jpg', cropped_img)

    # Convert to Grayscale
    pimg = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-2-gray.jpg', pimg)

    # Scale Up cropped text to make detection easier for Tesseract
    pimg = cv2.resize(pimg, dsize=(
        int(pimg.shape[1]*3), int(pimg.shape[0]*3)))

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-3-scaled.jpg', pimg)

    # Adjust image white levels for feature isolation
    pimg = cv2.addWeighted(pimg, 1.8, pimg, 0, -102)

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-4-contrast.jpg', pimg)

    # Feature isolation: Detect black space and crop it
    coords = cv2.findNonZero(pimg)
    x, y, w, h = cv2.boundingRect(coords)
    if(w == 0 or h == 0):
        return None
    pimg = pimg[y:y+h, x:x+w]
    pimg = cv2.copyMakeBorder(
        pimg, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-5-isolated.jpg', pimg)

    # Invert to White background and Black text
    pimg = cv2.bitwise_not(pimg)

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-6-flipped.jpg', pimg)

    # Filter fuzziness
    _, pimg = cv2.threshold(pimg, 240, 255, cv2.THRESH_BINARY)

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-7-filtered.jpg', pimg)

    # Sharpen borders
    element = cv2.getStructuringElement(
        shape=cv2.MORPH_RECT, ksize=(3, 3))
    pimg = cv2.erode(pimg, element, 3)

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-8-sharpen.jpg', pimg)

    # Process image into text using Tesseract
    e_text = ""
    if(is_name == True):
        e_text = pytesseract.image_to_string(
            pimg, lang='eng', config='--psm 6 -c tessedit_char_blacklist=!').strip()
    else:
        e_text = pytesseract.image_to_string(
            pimg, lang='eng', config='--psm 13 --oem 1 -c tessedit_char_whitelist=0123456789.').strip()

    if debug:
        screenshot = cv2.rectangle(
            screenshot, (rect.x1, rect.y1), (rect.x2, rect.y2), (0, 255, 255), 2)
    return e_text


def get_rarity(screenshot, rect: Rect, debug: bool = False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> int:
    """
    Detect Rarity inside rect within the screenshot based on color
    - 0 = Normal
    - 1 = Uncommon
    - 2 = Rare
    - 3 = Epic
    - 4 = Legendary
    - 5 = Relic
    """
    # Get sample rect from the bottom left corner
    sample_rect = Rect(rect.x1, rect.y2, rect.x1, rect.y2).add(-5, -5, 5, 5)

    # Crop image
    rarity_img = screenshot[sample_rect.y1:sample_rect.y2,
                            sample_rect.x1:sample_rect.x2]

    if debug:
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-9-rarity-sample.jpg', rarity_img)

    # Convert into Hue Saturation Vibrance
    rarity_img = cv2.cvtColor(rarity_img, cv2.COLOR_BGR2HSV)

    # Split values and keep Hue and Saturation
    rarity_img_h, rarity_img_s, _ = cv2.split(rarity_img)

    if debug:
        screenshot = cv2.rectangle(
            screenshot, (sample_rect.x1, sample_rect.y1), (sample_rect.x2, sample_rect.y2), (255, 255, 255), 1)
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-9-rarity-hue.jpg', rarity_img_h)
        cv2.imwrite(
            f'debug/inspection/text-{rect.y1}-{rect.x1}-9-rarity-saturation.jpg', rarity_img_s)

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


def process_line_column(screenshot, tab, anchor, line_index, column_index, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> typing.Tuple[int, str | None] | (str | None):
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
            screenshot, rect, debug, log_cb, error_cb)
        item = get_text(
            screenshot, rect, True, debug, log_cb, error_cb)
        return rarity, item
    else:
        return get_text(
            screenshot, rect, False, debug, log_cb, error_cb)


def process_line(screenshot, tab, anchor, line_index, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> MarketLine | None:
    """Process line columns using multithreading"""
    # Initialize executor and futures list
    column_futures = []
    executor = ThreadPoolExecutor(max_workers=5)

    # Push tasks and wait for them to finish
    for column_index in range(5):
        column_futures.append(executor.submit(
            process_line_column, screenshot, tab, anchor, line_index, column_index, debug, log_cb, error_cb))
    wait(column_futures)

    # Consolidate results
    columns = [column_future.result() for column_future in column_futures]

    # Item name cleanup
    name = columns[0][1]

    if name is None:
        return None

    if debug:
        log_cb(f"Raw Name: {name}")

    name = re.sub(f"\n*[\(\[]Sold in bundles.*", "", name)

    name = re.sub(f"\n*[\(\[]Untradable upon.*", "", name)

    if debug:
        log_cb(f"Filtered Name: {name}")
        log_cb(f"=================================")

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


def process_market_table(screenshot, tab, anchor, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> typing.List[MarketLine]:
    """Process market table using multithreading"""
    # Initialize executor and futures list
    line_futures = []
    executor = ThreadPoolExecutor(max_workers=2)

    # Push tasks and wait for them to finish
    for line_index in range(10):
        line_futures.append(executor.submit(
            process_line, screenshot, tab, anchor, line_index, debug, log_cb, error_cb))
    wait(line_futures)

    if debug:
        cv2.imwrite('debug/4-processed-screenshot.jpg', screenshot)

    # Consolidate results
    return [line_future.result() for line_future in line_futures if line_future.result()]


def match_market(screenshot, tab="market", debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> typing.Tuple[float, typing.Tuple[int, int]]:
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
    screenshot_hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

    # Split screenshot and keep Vibrance
    _, _, screenshot_v = cv2.split(
        screenshot_hsv)

    # Perform match template and keep the conficence value and location of the match
    res = cv2.matchTemplate(
        screenshot_v, sample_v, cv2.TM_CCOEFF_NORMED)
    _, maxVal, _, maxLoc = cv2.minMaxLoc(res)

    if debug == True:
        print(f"{tab}: {maxVal}")
        if maxVal > threshold:
            screenshot = cv2.rectangle(
                screenshot, (maxLoc[0], maxLoc[1]), (maxLoc[0]+sample.shape[1], maxLoc[1]+sample.shape[0]), (0, 0, 255), 2)
            log_cb(f"Found Market tab: {tab}")

    return maxVal, maxLoc, tab


def detect_market(screenshot, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> typing.Tuple[str, Point]:
    """Detect which market tab is open"""

    # Get confidence values for matching either search tab or interest tab
    matches = []
    matches.append(match_market(
        screenshot, "interest", debug, log_cb, error_cb))

    matches.append(match_market(
        screenshot, "market", debug, log_cb, error_cb))

    matches.append(match_market(
        screenshot, "buy_crystals", debug, log_cb, error_cb))

    matches.append(match_market(
        screenshot, "purchase_gold", debug, log_cb, error_cb))

    match_conf, loc, tab = max(matches, key=itemgetter(0))

    if(match_conf < threshold):
        raise Exception('NO_MARKET')

    return tab, Point(loc[0], loc[1])


def crop_image(screenshot, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)):
    """Remove black bars surrounding screenshot"""

    screenshot_middle = int(screenshot.shape[1] / 2)
    crop_detect_sc = screenshot[0:screenshot.shape[0],
                                screenshot_middle-int(screenshot.shape[1]/4):screenshot_middle+int(screenshot.shape[1]/4)]

    if debug:
        cv2.imwrite('debug/2.1-crop_detect_sc.jpg', crop_detect_sc)

    res = cv2.cvtColor(crop_detect_sc, cv2.COLOR_BGR2GRAY)
    res = cv2.addWeighted(res, 1.8, res, 0, -20)

    if debug:
        cv2.imwrite('debug/2.2-crop_detect_sc_contrast.jpg', res)

    coords = cv2.findNonZero(res)
    x, y, w, h = cv2.boundingRect(coords)
    screenshot = screenshot[y:y+h, 0:screenshot.shape[1]]

    if debug:
        cv2.imwrite('debug/2.3-cropped-screenshot.jpg', screenshot)

    return screenshot


def resize_screenshot(screenshot, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)):
    """Standarize screenshot size for matching"""

    scale = {
        'x': screenshot.shape[1] / scanMap['baseRes']['x'],
        'y': screenshot.shape[0] / scanMap['baseRes']['y']
    }

    resized = cv2.resize(screenshot, dsize=(
        int(screenshot.shape[1] / scale['y']), int(screenshot.shape[0] / scale['y'])))

    if debug:
        cv2.imwrite('debug/3-resized-screenshot.jpg', resized)

    return resized


def process_crystal_table(screenshot, tab, anchor, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)):
    rect_start = Point(
        x=int(anchor.x + scanMap[tab]['x']),
        y=int(anchor.y + (scanMap[tab]['y']))
    )
    rect = Rect(rect_start.x, rect_start.y,
                rect_start.x + scanMap[tab]['w'], rect_start.y + scanMap[tab]['h'])

    price = int(get_text(screenshot, rect, False, debug, log_cb, error_cb))

    if debug:
        screenshot = cv2.rectangle(
            screenshot, (rect.x1, rect.y1), (rect.x2, rect.y2), (255, 255, 255), 1)
        cv2.imwrite('debug/4-processed-screenshot.jpg.jpg', screenshot)

    match tab:
        case "purchase_gold":
            name = "Royal Crystal"
            log_cb(f"Raw - {name}: {price}")
            price = round(price/238, 2)
        case "buy_crystals":
            name = "Blue Crystal"
            log_cb(f"Raw - {name}: {price}")
            price = round(price/95, 2)

    return [MarketLine(0, name, price, price, price, 1)]


def scan(filepath, debug=False, log_cb=lambda log_txt: print(log_txt), error_cb=lambda error_txt: print(error_txt)) -> typing.List[MarketLine]:
    """Scan market screenshot"""
    if debug:
        log_cb('Directories cleanup')
        rmtree('debug')
        os.mkdir('debug')
        os.mkdir('debug/inspection')
    # Load screenshot
    screenshot = cv2.imread(filepath)

    if debug:
        cv2.imwrite('debug/1-screenshot.jpg', screenshot)

    # Crop black borders
    screenshot = crop_image(screenshot, debug, log_cb, error_cb)

    # Resize into measurements scale
    screenshot = resize_screenshot(screenshot, debug, log_cb, error_cb)

    # Detect which Market tab is open
    tab, anchor = detect_market(screenshot, debug, log_cb, error_cb)

    match tab:
        case "market":
            return process_market_table(screenshot, tab, anchor, debug, log_cb, error_cb)
        case "interest":
            return process_market_table(screenshot, tab, anchor, debug, log_cb, error_cb)
        case "buy_crystals":
            return process_crystal_table(screenshot, tab, anchor, debug, log_cb, error_cb)
        case "purchase_gold":
            return process_crystal_table(screenshot, tab, anchor, debug, log_cb, error_cb)
    # Process market tab
