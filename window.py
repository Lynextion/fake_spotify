
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox, 
    QApplication, QVBoxLayout)

from PyQt5.QtGui import QIcon 
from PyQt5 import QtMultimedia as M
import threading
import time
import os


import main2

class Ui_MainWindow(object):
    def __init__(self):
        self.player = main2.player()
        self.music_titles = []
        self.music_href = []
        self.index = ""
        self.music_player = M.QMediaPlayer()
        self.searched = ""
        

    def setupUi(self, MainWindow):
        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       # self.img = QtWidgets.QLabel(self.centralwidget)
        #self.img.setGeometry(QtCore.QRect(100, 90, 511, 251))
        #self.img.setObjectName("img")




        self.currentTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.currentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.currentTimeLabel.setGeometry(QtCore.QRect(70, 325, 61, 90))

        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeSlider.setGeometry(QtCore.QRect(550, 440, 61, 22))

        self.timeSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.timeSlider.setGeometry(QtCore.QRect(160, 360, 481, 22))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)


        self.totalTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalTimeLabel.setGeometry(QtCore.QRect(650,325,61,90))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)

        self.list=QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(100, 90, 511, 251))
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(350, 440, 61, 41))
        self.Play.setObjectName("Play")
        self.Play.clicked.connect(self.Start)
        self.pause_bt = QtWidgets.QPushButton(self.centralwidget)
        self.pause_bt.setGeometry(QtCore.QRect(420,440,61,41))
        self.pause_bt.setObjectName('Pause')
        self.pause_bt.clicked.connect(self.Pause)
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(310, 450, 31, 31))
        self.Next.setObjectName("Next")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(156, 390, 421, 31))
        self.label_title.setObjectName("label_title")
        self.Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(172, 20, 411, 20))
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
        #self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        #self.horizontalSlider.setGeometry(QtCore.QRect(160, 360, 481, 22))
        #self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        #self.horizontalSlider.setObjectName("horizontalSlider")
    
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Search_button.clicked.connect(self.search_clicked)
        self.list.clicked.connect(self.list_OnClicked)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        self.currentTimeLabel.setText(self._translate("MainWindow", "0:00"))
        MainWindow.setWindowTitle(self._translate("MainWindow", "Fake Spotify"))
        #self.img.setText(self._translate("MainWindow", "TextLabel"))
        self.Play.setText(self._translate("MainWindow", "Play"))
        self.Next.setText(self._translate("MainWindow", "Next"))
        self.pause_bt.setText(self._translate("MainWindow","Pause"))
        self.Search_button.setText(self._translate("MainWindow", "Search"))
        self.label_title.setText(self._translate("MainWindow", "Download complete"))
        self.music_player.durationChanged.connect(self.update_duration)
        self.music_player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.music_player.setPosition)
        self.volumeSlider.valueChanged.connect(self.music_player.setVolume)
    
    def Start(self):
        self.music_player.play()
    def Pause(self):
        self.music_player.pause()

    #ilk bu çalışacak
    def search_clicked(self):
        self.searched =  self.Search.text()
        self.thread =threading.Thread(target=self.player.search, args = (self.searched,))
        self.thread.start()
        self.insert_list()

    #buna basıldığında şarkı açılması lazım
    def insert_list(self):
        self.list.clear()
        self.music_titles,self.music_href = self.player.chrome()
        cache = ""
    
         
        for title in self.music_titles:
             title = title.strip()
    
             if cache != title:
                 self.list.addItem(title)
             cache = title
    
    #when user click the  listwiew
    def list_OnClicked(self):
        self.thread = threading.Thread(target = self.play_music)
        self.thread.start()


    def set_label_title(self):
        self.label_title.setText(self._translate("MainWindow",self.music_titles[self.index]))
        
        #play music thread
    def play_music(self):
        self.index = self.list.row(self.list.currentItem())
        print(self.music_href[self.index],"index",self.index)
        name = self.player.music_choose(self.music_href[self.index],self.music_titles[self.index].strip() + ".mp4")
        self.url = QtCore.QUrl.fromLocalFile(name)
        self.content = M.QMediaContent(self.url)
        self.music_player.setMedia(self.content)
        self.music_player.play()

    def update_duration(self,duration):
        print("!", duration)
        print("?", self.music_player.duration())
 
        self.timeSlider.setMaximum(duration)
        if duration >= 0:
            self.totalTimeLabel.setText(self.hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(self.hhmmss(position))

        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)
    
    def hhmmss(self,ms):
        s = round(ms / 1000)
        m,s = divmod(s,60)
        h,m = divmod(m,60)
        return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

