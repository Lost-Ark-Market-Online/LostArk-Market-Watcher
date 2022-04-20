import cv2
import pytesseract
import os

from modules.process import process_items
pytesseract.pytesseract.tesseract_cmd = os.path.abspath(os.path.join(os.path.dirname(__file__),'../lib/Tesseract-OCR/tesseract'))

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


def scan(filepath, _debug=False):
    debug = _debug

    def matchSearchMarket(screenshoot):
        screenshoot = screenshoot.copy()
        t_interest = cv2.imread(os.path.abspath(os.path.join(os.path.dirname(__file__),'../assets/search_market.jpg')))
        t_interest = cv2.cvtColor(t_interest, cv2.COLOR_BGR2HSV)
        t_interest_h, t_interest_s, t_interest_v = cv2.split(t_interest)

        if debug:
            cv2.imwrite(
                f'debug/areas/matchSearchMarket_interest_h.jpg', t_interest_h)
            cv2.imwrite(
                f'debug/areas/matchSearchMarket_interest_s.jpg', t_interest_s)
            cv2.imwrite(
                f'debug/areas/matchSearchMarket_interest_v.jpg', t_interest_v)

        screenshoot_hsv = cv2.cvtColor(screenshoot, cv2.COLOR_BGR2HSV)
        screenshoot_h, screenshoot_s, screenshoot_v = cv2.split(
            screenshoot_hsv)

        if debug:
            cv2.imwrite(f'debug/areas/matchSearchMarket_h.jpg', screenshoot_h)
            cv2.imwrite(f'debug/areas/matchSearchMarket_s.jpg', screenshoot_s)
            cv2.imwrite(f'debug/areas/matchSearchMarket_v.jpg', screenshoot_v)

        res = cv2.matchTemplate(
            screenshoot_v, t_interest_v, cv2.TM_CCOEFF_NORMED)
        _, maxVal, _, maxLoc = cv2.minMaxLoc(res)

        return maxVal, maxLoc

    def matchInterestList(screenshoot):
        screenshoot = screenshoot.copy()
        t_interest = cv2.imread(os.path.abspath(os.path.join(os.path.dirname(__file__),'../assets/interest_market.jpg')))
        t_interest = cv2.cvtColor(t_interest, cv2.COLOR_BGR2HSV)
        t_interest_h, t_interest_s, t_interest_v = cv2.split(t_interest)

        if debug:
            cv2.imwrite(
                f'debug/areas/matchInterestList_interest_h.jpg', t_interest_h)
            cv2.imwrite(
                f'debug/areas/matchInterestList_interest_s.jpg', t_interest_s)
            cv2.imwrite(
                f'debug/areas/matchInterestList_interest_v.jpg', t_interest_v)

        screenshoot_hsv = cv2.cvtColor(screenshoot, cv2.COLOR_BGR2HSV)
        screenshoot_h, screenshoot_s, screenshoot_v = cv2.split(
            screenshoot_hsv)

        if debug:
            cv2.imwrite(f'debug/areas/matchInterestList_h.jpg', screenshoot_h)
            cv2.imwrite(f'debug/areas/matchInterestList_s.jpg', screenshoot_s)
            cv2.imwrite(f'debug/areas/matchInterestList_v.jpg', screenshoot_v)

        res = cv2.matchTemplate(
            screenshoot_v, t_interest_v, cv2.TM_CCOEFF_NORMED)
        _, maxVal, _, maxLoc = cv2.minMaxLoc(res)
        return maxVal, maxLoc

    def adjust_contrast_brightness(img, contrast: float = 1.0, brightness: int = 0):
        brightness += int(round(255*(1-contrast)/2))
        return cv2.addWeighted(img, contrast, img, 0, brightness)

    def process_cropped(screenshoot, rec, i, a):
        recX1, recY1, recX2, recY2 = rec
        cropped_img = screenshoot[recY1:recY2, recX1:recX2]
        pimg = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
        pimg = cv2.resize(pimg, dsize=(
            int(pimg.shape[1]*3), int(pimg.shape[0]*3)))
        pimg = adjust_contrast_brightness(pimg, 1.8)
        coords = cv2.findNonZero(pimg)
        x, y, w, h = cv2.boundingRect(coords)
        if(w == 0 or h == 0):
            return None
        pimg = pimg[y:y+h, x:x+w]
        pimg = cv2.copyMakeBorder(
            pimg, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
        pimg = cv2.bitwise_not(pimg)

        _, pimg = cv2.threshold(pimg, 240, 255, cv2.THRESH_BINARY)

        element = cv2.getStructuringElement(
            shape=cv2.MORPH_RECT, ksize=(3, 3))

        pimg = cv2.erode(pimg, element, 3)

        if debug:
            cv2.imwrite(f'debug/cropped/img-{i}-{a}.jpg', pimg)

        e_text = None
        if(a == 0):
            e_text = pytesseract.image_to_string(
                pimg, lang='eng', config='--psm 6 -c tessedit_char_blacklist=!')
        else:
            e_text = pytesseract.image_to_string(
                pimg, lang='eng', config='--psm 13 --oem 1 -c tessedit_char_whitelist=0123456789,.')

        return e_text

    screenshoot = cv2.imread(filepath)

    scale = {
        'x': screenshoot.shape[1] / scanMap['baseRes']['x'],
        'y': screenshoot.shape[0] / scanMap['baseRes']['y']
    }

    screenshoot = cv2.resize(screenshoot, dsize=(
        int(screenshoot.shape[1] / scale['x']), int(screenshoot.shape[0] / scale['y'])))

    interest_list_conf, interest_list_loc = matchInterestList(screenshoot)
    search_market_conf, search_market_loc = matchSearchMarket(screenshoot)

    loc = None
    tab = None
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

    if (loc is not None):
        MPx, MPy = loc
        screenshoot = cv2.rectangle(
            screenshoot, (MPx, MPy), (MPx+20, MPy+20), (255, 0, 0), 2)

        text = []
        for i in range(10):
            line = []
            for a in range(5):
                recX1 = int(MPx + scanMap[tab]
                            ['xItemStops'][a])
                recY1 = int(MPy + (scanMap[tab]['yMargin']) +
                            i*scanMap[tab]['yItemSpacing'])
                recX2 = int(recX1 +
                            scanMap[tab]['xItemWidths'][a])
                recY2 = int(recY1 + scanMap[tab]
                            ['itemHeight'])

                item = process_cropped(
                    screenshoot, (recX1, recY1, recX2, recY2), i, a)

                if item is None:
                    break

                line.append(item)
                screenshoot = cv2.rectangle(
                    screenshoot, (recX1, recY1), (recX2, recY2), (255, 0, 0), 2)
            if len(line) > 0:
                text.append(line)
        if debug:
            cv2.imwrite(f'debug/areas/screenshoot.jpg', screenshoot)
        return process_items(text)
