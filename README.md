## LostArk Market Watcher 0.1.1
This app listens to the screenshot folder for new files.
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
- ConfigParser `pip install configparser`
- EasyGui `pip install easygui`
- Google Cloud Firestore `pip install google-cloud-firestore`
- Simpleaudio `pip install simpleaudio`

### Assets
Audio files from [MixKit](https://mixkit.co/)

---
[LostArkMarket](https://lostarkmarket-79ddf.web.app/)