# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(300, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chatTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.chatTextEdit.setReadOnly(True)
        self.chatTextEdit.setObjectName("chatTextEdit")
        self.verticalLayout.addWidget(self.chatTextEdit)
        self.msgAreaEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.msgAreaEdit.setObjectName("msgAreaEdit")
        self.verticalLayout.addWidget(self.msgAreaEdit)
        self.sendMsgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendMsgBtn.setObjectName("sendMsgBtn")
        self.verticalLayout.addWidget(self.sendMsgBtn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chatTextEdit.setPlaceholderText(_translate("MainWindow", "Тут будут сообщения"))
        self.msgAreaEdit.setPlaceholderText(_translate("MainWindow", "Введите ваше сообщение"))
        self.sendMsgBtn.setText(_translate("MainWindow", "Send message"))


