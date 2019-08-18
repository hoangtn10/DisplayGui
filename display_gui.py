import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import *

my_app = QApplication(sys.argv)
my_web = QWebEngineView()

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
local_url = QUrl.fromLocalFile(file_path)
my_web.load(local_url)
my_web.resize(1000, 600)
my_web.show()
sys.exit(my_app.exec_())
