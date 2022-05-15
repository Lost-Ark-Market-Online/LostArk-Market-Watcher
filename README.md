## LostArk Market Watcher 0.7.6
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
- TheFuzz `pip install thefuzz[speedup]`
- lxml `pip install lxml`
- pycaw `pip install pycaw`

### Assets
Audio files from [MixKit](https://mixkit.co/)

### Changelog
### 0.7.6
- Bugfix: Config modal open segmentation fault

### 0.7.5
- Bugfix: Configuration handling

### 0.7.4
- Bugfix: soft game detection config set

### 0.7.3
- Soft config set

### 0.7.2
- Tolerant fail check for Volume controller
- Tolerant fail check for Game directory config

### 0.7.1
- Fix win32api dependency, changed to ctypes windll
- Remove window flashes

### 0.7.0
- Add Threading controls to config
- Add Volume controls to config
- Add Region checking
- Add Game folder detection
- Upgrade Message box handling
- Upgrade Config handling
- Add Single app execution check

### 0.6.3
- Image naming standarization update

### 0.6.2
- App windows fixes and live notification on new version published

### 0.6.1
- Change diff based string matching to Levenshtein Distance using TheFuzz

### 0.6.0
- Add support for Scanning Blue Crystal and Royal Crystal prices from Currency Exchange

### 0.5.1
- lower strict entry rules, now avg price is optional and filled with lower price

### 0.5.0
- Added new items compatibility. We can now scan anything but Skins.

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
