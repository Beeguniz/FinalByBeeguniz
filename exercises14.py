# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercises14.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1008)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1911, 1011))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 961, 1011))
        self.widget_2.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 182, 120, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(60, 480, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.q2 = QtWidgets.QLabel(self.widget_2)
        self.q2.setGeometry(QtCore.QRect(160, 460, 681, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.q2.setFont(font)
        self.q2.setMouseTracking(False)
        self.q2.setTabletTracking(False)
        self.q2.setAcceptDrops(False)
        self.q2.setAutoFillBackground(False)
        self.q2.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q2.setScaledContents(False)
        self.q2.setWordWrap(True)
        self.q2.setObjectName("q2")
        self.ans14_2_1 = QtWidgets.QComboBox(self.widget_2)
        self.ans14_2_1.setGeometry(QtCore.QRect(280, 480, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_2_1.setFont(font)
        self.ans14_2_1.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_2_1.setObjectName("ans14_2_1")
        self.ans14_2_1.addItem("")
        self.ans14_2_1.addItem("")
        self.ans14_2_1.addItem("")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(60, 720, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.check14_1 = QtWidgets.QPushButton(self.widget_2)
        self.check14_1.setGeometry(QtCore.QRect(360, 320, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check14_1.setFont(font)
        self.check14_1.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check14_1.setObjectName("check14_1")
        self.check14_2 = QtWidgets.QPushButton(self.widget_2)
        self.check14_2.setGeometry(QtCore.QRect(410, 580, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check14_2.setFont(font)
        self.check14_2.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check14_2.setObjectName("check14_2")
        self.q2_2 = QtWidgets.QLabel(self.widget_2)
        self.q2_2.setGeometry(QtCore.QRect(160, 700, 721, 131))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.q2_2.setFont(font)
        self.q2_2.setMouseTracking(False)
        self.q2_2.setTabletTracking(False)
        self.q2_2.setAcceptDrops(False)
        self.q2_2.setAutoFillBackground(False)
        self.q2_2.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q2_2.setScaledContents(False)
        self.q2_2.setWordWrap(True)
        self.q2_2.setObjectName("q2_2")
        self.check14_3 = QtWidgets.QPushButton(self.widget_2)
        self.check14_3.setGeometry(QtCore.QRect(410, 860, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check14_3.setFont(font)
        self.check14_3.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check14_3.setObjectName("check14_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(250, 30, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 20px;\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.back_gr14 = QtWidgets.QPushButton(self.widget_2)
        self.back_gr14.setGeometry(QtCore.QRect(30, 920, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_gr14.setFont(font)
        self.back_gr14.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.back_gr14.setObjectName("back_gr14")
        self.q1_3 = QtWidgets.QLabel(self.widget_2)
        self.q1_3.setGeometry(QtCore.QRect(150, 160, 561, 141))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.q1_3.setFont(font)
        self.q1_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.q1_3.setMouseTracking(True)
        self.q1_3.setTabletTracking(False)
        self.q1_3.setAcceptDrops(False)
        self.q1_3.setAutoFillBackground(False)
        self.q1_3.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q1_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.q1_3.setScaledContents(False)
        self.q1_3.setWordWrap(True)
        self.q1_3.setIndent(10)
        self.q1_3.setOpenExternalLinks(False)
        self.q1_3.setObjectName("q1_3")
        self.ans14_2_2 = QtWidgets.QComboBox(self.widget_2)
        self.ans14_2_2.setGeometry(QtCore.QRect(500, 480, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_2_2.setFont(font)
        self.ans14_2_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_2_2.setObjectName("ans14_2_2")
        self.ans14_2_2.addItem("")
        self.ans14_2_2.addItem("")
        self.ans14_2_2.addItem("")
        self.ans14_2_3 = QtWidgets.QComboBox(self.widget_2)
        self.ans14_2_3.setGeometry(QtCore.QRect(750, 720, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_2_3.setFont(font)
        self.ans14_2_3.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_2_3.setObjectName("ans14_2_3")
        self.ans14_2_3.addItem("")
        self.ans14_2_3.addItem("")
        self.ans14_2_3.addItem("")
        self.ans14_3_1 = QtWidgets.QComboBox(self.widget_2)
        self.ans14_3_1.setGeometry(QtCore.QRect(340, 720, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_3_1.setFont(font)
        self.ans14_3_1.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_3_1.setObjectName("ans14_3_1")
        self.ans14_3_1.addItem("")
        self.ans14_3_1.addItem("")
        self.ans14_3_1.addItem("")
        self.ans14_3_2 = QtWidgets.QComboBox(self.widget_2)
        self.ans14_3_2.setGeometry(QtCore.QRect(550, 720, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_3_2.setFont(font)
        self.ans14_3_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_3_2.setObjectName("ans14_3_2")
        self.ans14_3_2.addItem("")
        self.ans14_3_2.addItem("")
        self.ans14_3_2.addItem("")
        self.ans14_1_1 = QtWidgets.QComboBox(self.widget_2)
        self.ans14_1_1.setGeometry(QtCore.QRect(430, 180, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_1_1.setFont(font)
        self.ans14_1_1.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_1_1.setObjectName("ans14_1_1")
        self.ans14_1_1.addItem("")
        self.ans14_1_1.addItem("")
        self.ans14_1_1.addItem("")
        self.ans14_1_2 = QtWidgets.QComboBox(self.widget_2)
        self.ans14_1_2.setGeometry(QtCore.QRect(330, 240, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_1_2.setFont(font)
        self.ans14_1_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_1_2.setObjectName("ans14_1_2")
        self.ans14_1_2.addItem("")
        self.ans14_1_2.addItem("")
        self.ans14_1_2.addItem("")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(960, 0, 941, 1011))
        self.widget_3.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 182, 120, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:0, y2:1, stop:0 rgba(189, 182, 120, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(60, 100, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.q1_2 = QtWidgets.QLabel(self.widget_3)
        self.q1_2.setGeometry(QtCore.QRect(160, 60, 701, 131))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.q1_2.setFont(font)
        self.q1_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.q1_2.setMouseTracking(True)
        self.q1_2.setTabletTracking(False)
        self.q1_2.setAcceptDrops(False)
        self.q1_2.setAutoFillBackground(False)
        self.q1_2.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.q1_2.setScaledContents(False)
        self.q1_2.setWordWrap(True)
        self.q1_2.setObjectName("q1_2")
        self.ans14_4_2 = QtWidgets.QComboBox(self.widget_3)
        self.ans14_4_2.setGeometry(QtCore.QRect(530, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_4_2.setFont(font)
        self.ans14_4_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_4_2.setObjectName("ans14_4_2")
        self.ans14_4_2.addItem("")
        self.ans14_4_2.addItem("")
        self.ans14_4_2.addItem("")
        self.ans14_4_1 = QtWidgets.QComboBox(self.widget_3)
        self.ans14_4_1.setGeometry(QtCore.QRect(330, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_4_1.setFont(font)
        self.ans14_4_1.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_4_1.setObjectName("ans14_4_1")
        self.ans14_4_1.addItem("")
        self.ans14_4_1.addItem("")
        self.ans14_4_1.addItem("")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(50, 430, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.check14_4 = QtWidgets.QPushButton(self.widget_3)
        self.check14_4.setGeometry(QtCore.QRect(430, 240, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check14_4.setFont(font)
        self.check14_4.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check14_4.setObjectName("check14_4")
        self.check14_5 = QtWidgets.QPushButton(self.widget_3)
        self.check14_5.setGeometry(QtCore.QRect(420, 570, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check14_5.setFont(font)
        self.check14_5.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check14_5.setObjectName("check14_5")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(60, 740, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.q2_3 = QtWidgets.QLabel(self.widget_3)
        self.q2_3.setGeometry(QtCore.QRect(180, 720, 691, 131))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.q2_3.setFont(font)
        self.q2_3.setMouseTracking(False)
        self.q2_3.setTabletTracking(False)
        self.q2_3.setAcceptDrops(False)
        self.q2_3.setAutoFillBackground(False)
        self.q2_3.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q2_3.setScaledContents(False)
        self.q2_3.setWordWrap(True)
        self.q2_3.setObjectName("q2_3")
        self.ans14_6 = QtWidgets.QComboBox(self.widget_3)
        self.ans14_6.setGeometry(QtCore.QRect(720, 740, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_6.setFont(font)
        self.ans14_6.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_6.setObjectName("ans14_6")
        self.ans14_6.addItem("")
        self.ans14_6.addItem("")
        self.ans14_6.addItem("")
        self.check14_6 = QtWidgets.QPushButton(self.widget_3)
        self.check14_6.setGeometry(QtCore.QRect(410, 870, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check14_6.setFont(font)
        self.check14_6.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check14_6.setObjectName("check14_6")
        self.q1 = QtWidgets.QLabel(self.widget_3)
        self.q1.setGeometry(QtCore.QRect(180, 390, 601, 151))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.q1.setFont(font)
        self.q1.setMouseTracking(False)
        self.q1.setTabletTracking(False)
        self.q1.setAcceptDrops(False)
        self.q1.setAutoFillBackground(False)
        self.q1.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q1.setScaledContents(False)
        self.q1.setWordWrap(True)
        self.q1.setObjectName("q1")
        self.ans14_5 = QtWidgets.QComboBox(self.widget_3)
        self.ans14_5.setGeometry(QtCore.QRect(330, 470, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_5.setFont(font)
        self.ans14_5.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_5.setObjectName("ans14_5")
        self.ans14_5.addItem("")
        self.ans14_5.addItem("")
        self.ans14_5.addItem("")
        self.ans14_4_3 = QtWidgets.QComboBox(self.widget_3)
        self.ans14_4_3.setGeometry(QtCore.QRect(750, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans14_4_3.setFont(font)
        self.ans14_4_3.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans14_4_3.setObjectName("ans14_4_3")
        self.ans14_4_3.addItem("")
        self.ans14_4_3.addItem("")
        self.ans14_4_3.addItem("")
        self.nextp2_14 = QtWidgets.QPushButton(self.widget_3)
        self.nextp2_14.setGeometry(QtCore.QRect(810, 930, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.nextp2_14.setFont(font)
        self.nextp2_14.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.nextp2_14.setObjectName("nextp2_14")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.check14_1.clicked.connect(self.check_answer14_1)
        self.check14_2.clicked.connect(self.check_answer14_2)
        self.check14_3.clicked.connect(self.check_answer14_3)
        self.check14_4.clicked.connect(self.check_answer14_4)
        self.check14_5.clicked.connect(self.check_answer14_5)
        self.check14_6.clicked.connect(self.check_answer14_6)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.q2.setText(_translate("MainWindow", "ここ          トイレ          ありません。"))
        self.ans14_2_1.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_2_1.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_2_1.setItemText(2, _translate("MainWindow", "が"))
        self.label_5.setText(_translate("MainWindow", "3"))
        self.check14_1.setText(_translate("MainWindow", "Check"))
        self.check14_2.setText(_translate("MainWindow", "Check"))
        self.q2_2.setText(_translate("MainWindow", "シンさん        ホテル         まえ         います。"))
        self.check14_3.setText(_translate("MainWindow", "Check"))
        self.label.setText(_translate("MainWindow", "Question 1. Choose the correct word:"))
        self.back_gr14.setText(_translate("MainWindow", "Back"))
        self.q1_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.q1_3.setText(_translate("MainWindow", "わたしの　まち         きれいな　こうえん          あります。"))
        self.ans14_2_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_2_2.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_2_2.setItemText(2, _translate("MainWindow", "は"))
        self.ans14_2_3.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_2_3.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_2_3.setItemText(2, _translate("MainWindow", "の"))
        self.ans14_3_1.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_3_1.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_3_1.setItemText(2, _translate("MainWindow", "は"))
        self.ans14_3_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_3_2.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_3_2.setItemText(2, _translate("MainWindow", "の"))
        self.ans14_1_1.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_1_1.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_1_1.setItemText(2, _translate("MainWindow", "が"))
        self.ans14_1_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_1_2.setItemText(1, _translate("MainWindow", "が"))
        self.ans14_1_2.setItemText(2, _translate("MainWindow", "は"))
        self.label_6.setText(_translate("MainWindow", "4"))
        self.q1_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Noto Sans JP\',\'ヒラギノ角ゴ Pro W3\',\'Hiragino Kaku Gothic Pro\',\'メイリオ\',\'Meiryo\',\'ＭＳ Ｐゴシック\',\'sans-serif\'; font-size:20px; color:#717171; background-color:#fffdf7;\">テーブルの うえ           バナナ</span><span style=\" font-family:\'Noto Sans JP\',\'ヒラギノ角ゴ Pro W3\',\'Hiragino Kaku Gothic Pro\',\'メイリオ\',\'Meiryo\',\'ＭＳ Ｐゴシック\',\'sans-serif\'; font-size:20px; font-weight:400; color:#717171; background-color:#fffdf7;\"/><span style=\" font-family:\'Noto Sans JP\',\'ヒラギノ角ゴ Pro W3\',\'Hiragino Kaku Gothic Pro\',\'メイリオ\',\'Meiryo\',\'ＭＳ Ｐゴシック\',\'sans-serif\'; font-size:20px; color:#717171; background-color:#fffdf7;\">あります。</span></p><p><br/><span style=\" font-family:\'Noto Sans JP\'; font-size:18px; color:#717171;\"/><span style=\" font-family:\'Noto Sans JP\'; font-size:18px; font-weight:400; color:#717171;\"/><a name=\"ui-id-4-button\"/><a href=\"https://a1.marugotoweb.jp/en/grammar_topic6_11.php#nogo\"><span style=\" font-family:\'Verdana\',\'Arial\',\'sans-serif\'; font-size:20px; font-weight:400; color:#666666; background-color:#fffdf7; vertical-align:middle;\"><br/></span></a><span style=\" font-family:\'Noto Sans JP\'; font-size:18px; font-weight:400; color:#717171;\"/><a name=\"ui-id-4-button\"/><a href=\"https://a1.marugotoweb.jp/en/grammar_topic6_11.php#nogo\"><span style=\" font-family:\'Verdana\',\'Arial\',\'sans-serif\'; font-size:20px; font-weight:400; color:#666666; background-color:#fffdf7; vertical-align:middle;\"><br/></span></a></p></body></html>"))
        self.q1_2.setText(_translate("MainWindow", "ぎんこう          えき          ちかく        ありますか"))
        self.ans14_4_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_4_2.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_4_2.setItemText(2, _translate("MainWindow", "の"))
        self.ans14_4_1.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_4_1.setItemText(1, _translate("MainWindow", "の"))
        self.ans14_4_1.setItemText(2, _translate("MainWindow", "は"))
        self.label_7.setText(_translate("MainWindow", "5"))
        self.check14_4.setText(_translate("MainWindow", "Check"))
        self.check14_5.setText(_translate("MainWindow", "Check"))
        self.label_8.setText(_translate("MainWindow", "6"))
        self.q2_3.setText(_translate("MainWindow", "わたしは　きっさてんの　まえに　　　　　。"))
        self.ans14_6.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_6.setItemText(1, _translate("MainWindow", "あります"))
        self.ans14_6.setItemText(2, _translate("MainWindow", "います"))
        self.check14_6.setText(_translate("MainWindow", "Check"))
        self.q1.setText(_translate("MainWindow", "さいたまに　ゆうめいな　はくぶつかんが　　　　　　　。"))
        self.ans14_5.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_5.setItemText(1, _translate("MainWindow", "あります"))
        self.ans14_5.setItemText(2, _translate("MainWindow", "います"))
        self.ans14_4_3.setItemText(0, _translate("MainWindow", "?"))
        self.ans14_4_3.setItemText(1, _translate("MainWindow", "に"))
        self.ans14_4_3.setItemText(2, _translate("MainWindow", "の"))
        self.nextp2_14.setText(_translate("MainWindow", "Next"))

    def check_answer14_1(self):
        selected_answer14_1_1 = self.ans14_1_1.currentText()
        selected_answer14_1_2 = self.ans14_1_2.currentText()
        if selected_answer14_1_1 == 'に' and selected_answer14_1_2 == 'が':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()
    def check_answer14_2(self):
        selected_answer14_2_1 = self.ans14_2_1.currentText()
        selected_answer14_2_2 = self.ans14_2_2.currentText()
        if selected_answer14_2_1 == 'に' and selected_answer14_2_2 == 'は':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()

    def check_answer14_3(self):
        selected_answer14_3_1 = self.ans14_3_1.currentText()
        selected_answer14_3_2 = self.ans14_3_2.currentText()
        selected_answer14_3_4 = self.ans14_3_2.currentText()
        if selected_answer14_3_1 == 'は' and selected_answer14_3_2 == 'の' and selected_answer14_3_2 == 'に':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()
    def check_answer14_4(self):
        selected_answer14_4_1 = self.ans14_4_1.currentText()
        selected_answer14_4_2 = self.ans14_4_2.currentText()
        selected_answer14_4_3 = self.ans14_4_3.currentText()
        if selected_answer14_4_1 == 'は' and selected_answer14_4_2 =='の' and selected_answer14_4_3 =='に':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()
    def check_answer14_5(self):
        selected_answer14_5 = self.ans14_5.currentText()
        if selected_answer14_5 == 'あります':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()
    def check_answer14_6(self):
        selected_answer14_6 = self.ans14_6.currentText()
        if selected_answer14_6 == 'います':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
