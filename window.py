
from PyQt5 import QtCore, QtGui, QtWidgets
import main2

class Ui_MainWindow(object):
    def __init(self):
        player = main2.player()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(100, 90, 511, 251))
        self.img.setObjectName("img")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(350, 440, 61, 41))
        self.Play.setObjectName("Play")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(310, 450, 31, 31))
        self.Next.setObjectName("Next")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(156, 390, 421, 31))
        self.label_2.setObjectName("label_2")
        self.Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(192, 20, 411, 20))
        self.Search.setText("")
        self.Search.setObjectName("Search")
        self.Search_button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button.setGeometry(QtCore.QRect(630, 20, 75, 23))
        self.Search_button.setObjectName("Search_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Search_button.clicked.connect(self.search_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img.setText(_translate("MainWindow", "TextLabel"))
        self.Play.setText(_translate("MainWindow", "Play"))
        self.Next.setText(_translate("MainWindow", "Next"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.Search_button.setText(_translate("MainWindow", "Search"))
    
    def search_clicked(self):
      searched =  self.Search.text()
      player.search(searched)
      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

