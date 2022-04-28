## LostArk Market Watcher 0.4.2
This app listens to the screenshot folder for new files.
Starting on the version 0.3.0 this app needs to be launched through the [Lost Ark Market Launcher](https://github.com/gogodr/LostArk-Market-Launcher)
Each new file is scanned and if the market window is detected in the picture then the image is segmented.
Each segment then is parsed usin Tesseract OCR and classified
The information then is collected and published to the LostArk Marketplace firestore database.

In order to contribute to the LostArk Marketplace database, the contributor must be authenticated and aproved. 

### Limitations
Right now it only works on 1080p and 4K resolutions. 
Support for 21:9 is on the works.

### Dependencies
- TesseractOCR ( A compiled version for Windows x64 is included in this repository )
- PyTesseract `pip install pytesseract`
- OpenCV `pip install opencv-python`
- Pyside6 (Qt for Python) `pip install PySide6`
- Google Cloud Firestore `pip install google-cloud-firestore`
- Simpleaudio `pip install simpleaudio`
- Watchdog `pip install watchdog`
- Python Slugify `pip install python-slugify`

### Assets
Audio files from [MixKit](https://mixkit.co/)

### ToDo:
- Support for 21:9 aspect ratio
- Add Adventure Tome items
- Add Gold / Royal Crystal / Blue Crystal converstions support

### Changelog
### 0.4.1
- Enforce item rarity from dict before pushing

### 0.4.1
- Critical: Standarized document Ids

### 0.4.0
- Multi Threading optimization for scans and uploads

### 0.3.0
- Lost Ark Market Launcher integracion for automatic updates
- UI Revamp
- Threading optimizations
- Region autodetection
- Automatic market screenshot cleanup after scans


### 0.2.0
Added support for Engraving Recipes and Combat Items.

---
[LostArkMarket](https://www.lostarkmarket.online)
