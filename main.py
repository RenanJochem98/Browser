from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap

searchBarHeigth = 30
homeUrl = "https://www.google.com"

application = QApplication([])

mainWindow = QMainWindow()
mainWindow.setGeometry(0,0,1300,900)


mainWindow.setWindowTitle("Browser")
mainWindow.setStyleSheet("background-color: rgb(0,0,0);")

web = QWebEngineView(mainWindow)
web.setGeometry(0,searchBarHeigth,1300,900)
web.setStyleSheet("background-color: rgb(255,255,255);")
web.load(QUrl(homeUrl))

homeBtn = QToolButton(mainWindow)
homeBtn.setGeometry(10, 0,30, searchBarHeigth)
# homeBtn.setStyleSheet("background-color: transparent;")
homeBtn.setStyleSheet("background-color: rgb(255,0,0);")
homeBtn.setText("H")

reloadBtn = QToolButton(mainWindow)
reloadBtn.setGeometry(45, 0,30, searchBarHeigth)
# reloadBtn.setStyleSheet("background-color: transparent;")
reloadBtn.setStyleSheet("background-color: rgb(0,255,0);")
reloadBtn.setText("R")

backBtn = QToolButton(mainWindow)
backBtn.setGeometry(80, 0,30, searchBarHeigth)
# backBtn.setStyleSheet("background-color: transparent;")
backBtn.setStyleSheet("background-color: rgb(0,0,255);")
backBtn.setText("B")

goLine = QLineEdit(mainWindow)
goLine.setGeometry(125, 0,510, searchBarHeigth)
goLine.setStyleSheet("background-color: rgb(160,160,160);")

goBtn = QToolButton(mainWindow)
goBtn.setGeometry(670, 0,30, searchBarHeigth)
# goBtn.setStyleSheet("background-color: transparent;")
goBtn.setStyleSheet("background-color: rgb(255,255,0);")
goBtn.setText("Ir")

def home(mainWindow):
    web.load(QUrl(homeUrl))

def go(mainWindow):
    url = goLine.text()
    web.load(QUrl(url))

def download(item):
    item.accept()
    msg = QMessageBox()
    msg.setWindowTitle("Download")
    msg.setText("Download iniciado")
    msg.exec_()

homeBtn.clicked.connect(home)
goBtn.clicked.connect(go)
web.page().profile().downloadRequested.connect(download)
if __name__ == "__main__":
    mainWindow.show()
    application.exec()
