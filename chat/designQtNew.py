# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat/main_window.ui',
# licensing of 'chat/main_window.ui' applies.
#
# Created: Fri Jul  5 23:42:24 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(298, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(300, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat_text = QtWidgets.QTextEdit(self.centralwidget)
        self.chat_text.setStyleSheet("QTextEdit {\n"
"  display: grid;\n"
"  align-content: end;\n"
"  align-items: end;\n"
"  justify-content: end;\n"
"  flex-grow: 1;\n"
"  padding: 15px 20px 24px 30px;\n"
"  overflow: auto;\n"
"\n"
"  background-color: #5c8ab3;\n"
"}")
        self.chat_text.setReadOnly(True)
        self.chat_text.setObjectName("chat_text")
        self.verticalLayout.addWidget(self.chat_text)
        self.message_area = QtWidgets.QLineEdit(self.centralwidget)
        self.message_area.setStyleSheet("QLineEdit {\n"
"\n"
"  box-sizing: border-box;\n"
"  padding: 9px 20px 11px;\n"
"\n"
"  border: 2px solid #ffffff;\n"
"  background-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #ccc;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border-color: #56cf4c;\n"
"  outline: none;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border-color: #9edcff;\n"
"  outline: none;\n"
"}")
        self.message_area.setObjectName("message_area")
        self.verticalLayout.addWidget(self.message_area)
        self.send_message_button = QtWidgets.QLineEdit(self.centralwidget)
        self.send_message_button.setStyleSheet("QLineEdit {\n"
"\n"
"  border-radius: 50px;\n"
"  background-color: #39b54a;\n"
"  padding: 9px 20px;\n"
"\n"
"  color: #ffffff;\n"
"\n"
"  background-color: #39b54a;\n"
"  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.15);\n"
"  border: 2px solid transparent;\n"
"\n"
"  user-select: none;\n"
"  outline: none;\n"
"  touch-action: manipulation;\n"
"  cursor: pointer; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  background-color: #56cf4c;\n"
"  box-shadow: 0 8px 4px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border-color: 2px solid #9edcff;\n"
"}\n"
"")
        self.send_message_button.setObjectName("send_message_button")
        self.verticalLayout.addWidget(self.send_message_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.chat_text.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Тут будут сообщения", None, -1))
        self.message_area.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Введите ваше сообщение", None, -1))
        self.send_message_button.setText(QtWidgets.QApplication.translate("MainWindow", "Отправить сообщение", None, -1))

