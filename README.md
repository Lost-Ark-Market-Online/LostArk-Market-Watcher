## LostArk Market Watcher 0.4.12
This app listens to the screenshot folder for new files.
Starting on the version 0.3.0 this app needs to be launched through the [Lost Ark Market Launcher](https://github.com/gogodr/LostArk-Market-Launcher)
Each new file is scanned and if the market window is detected in the picture then the image is segmented.
Each segment then is parsed usin Tesseract OCR and classified
The information then is collected and published to the LostArk Marketplace firestore database.

In order to contribute to the LostArk Marketplace database, the contributor must be authenticated and aproved. 

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

### Changelog
### 0.4.12
- Make name filter classificator fuzzier

### 0.4.11
- Link error logs from db instance

### 0.4.10
- Update cropping algorithm: adjust tolerances

### 0.4.9
- Stricter validation and more metadata for updates and entries

### 0.4.8
- Price validation before pushing

### 0.4.7
- Bugfix: Overlays support for 21:9 forced resolution
- Move integrity metadata input from cloud function to watcher client

### 0.4.6
- Bugfix: Refresh season token every 30 minutes
- Log: Scroll to bottom automatically

### 0.4.5
- Add Adventure Tome items

### 0.4.4
- Add a logger window and option to write the log into files

### 0.4.3
- Support for multiple aspect ratios

### 0.4.2
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
