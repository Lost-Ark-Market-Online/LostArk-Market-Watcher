import os
from shutil import rmtree
from PySide6.QtWidgets import QApplication, QFileDialog
from modules.logging import AppLogger
from modules.scan import scan_file

app = QApplication([])
file,_ = QFileDialog.getOpenFileName(None,
                                      "Select the Lost Ark Screenshot to test", None, "Image Files (*.jpg)")
if file:
  
  AppLogger().debug('Directories cleanup')
  if os.path.isdir('debug'):
      rmtree('debug')
  os.mkdir('debug')
  scan = scan_file(file)

  print(scan)