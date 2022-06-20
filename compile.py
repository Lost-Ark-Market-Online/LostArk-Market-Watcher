import os
from modules.config import Config


Config().version

if Config().debug:
  os.system(f'python -m nuitka --standalone --windows-icon-from-ico=assets/icons/favicon.ico --enable-plugin=pyside6 --enable-plugin=numpy --include-package-data=grpc --include-package-data=text_unidecode --include-data-dir=assets=assets --include-data-dir=lib=lib --follow-imports  --onefile --windows-file-version={Config().version} --windows-product-version={Config().version} --windows-company-name="Lost Ark Market Online" --windows-product-name="Lost Ark Market Online Watcher App" --windows-file-description="Lost Ark Market Online Watcher App" -o lamo-watcher-debug.exe index.py')
else:
  os.system(f'python -m nuitka --standalone --windows-icon-from-ico=assets/icons/favicon.ico --enable-plugin=pyside6 --enable-plugin=numpy --include-package-data=grpc --include-package-data=sentry_sdk --include-package-data=text_unidecode --include-data-dir=assets=assets --include-data-dir=lib=lib --follow-imports --onefile --windows-disable-console --windows-file-version={Config().version} --windows-product-version={Config().version} --windows-company-name="Lost Ark Market Online" --windows-product-name="Lost Ark Market Online Watcher App" --windows-file-description="Lost Ark Market Online Watcher App" -o lamo-watcher.exe index.py')