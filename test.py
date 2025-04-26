from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import os

app = QApplication(sys.argv)

label = QLabel()
img_path = os.path.join(os.path.dirname(__file__), "Media", "WKImage.png")
pixmap = QPixmap(img_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

label.setPixmap(pixmap)
label.setFixedSize(100, 100)
label.show()

sys.exit(app.exec_())
