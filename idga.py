# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idga.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_search = QtWidgets.QPushButton(self.centralwidget)
        self.start_search.setGeometry(QtCore.QRect(290, 50, 75, 23))
        self.start_search.setObjectName("start_search")
        self.search_text = QtWidgets.QLineEdit(self.centralwidget)
        self.search_text.setGeometry(QtCore.QRect(32, 50, 241, 21))
        self.search_text.setText("")
        self.search_text.setObjectName("search_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 141, 16))
        self.label_2.setObjectName("label_2")
        self.result_textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.result_textbox.setGeometry(QtCore.QRect(290, 120, 211, 131))
        self.result_textbox.setReadOnly(True)
        self.result_textbox.setObjectName("result_textbox")
        self.results_list = QtWidgets.QListWidget(self.centralwidget)
        self.results_list.setGeometry(QtCore.QRect(30, 120, 231, 131))
        self.results_list.setObjectName("results_list")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(430, 280, 75, 23))
        self.exit_button.setObjectName("exit_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_search.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Search for"))
        self.label_2.setText(_translate("MainWindow", "Results"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))

