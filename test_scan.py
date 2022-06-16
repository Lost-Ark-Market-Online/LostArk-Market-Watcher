from PySide6.QtWidgets import QApplication, QFileDialog
from modules.scan import scan

app = QApplication([])
file,_ = QFileDialog.getOpenFileName(None,
                                      "Select the Lost Ark Screenshot to test", None, "Image Files (*.jpg)")
if file:
  market_lines = scan(file)

  print(market_lines)