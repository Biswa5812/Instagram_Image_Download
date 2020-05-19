# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insta.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(481, 228)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 231, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 140, 111, 28))
        self.pushButton.setObjectName("pushButton")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 190, 211, 21))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Instagram Image Downloader"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-style:italic; color:#ffffff;\">Insta_D</span></p></body></html>"))

        self.label_2.setText(_translate("Form", "Image Url"))

        self.pushButton.setText(_translate("Form", "Start Download"))
        self.pushButton.clicked.connect(self.download)

    def download(self):
        url = self.lineEdit.text()
        url_a = requests.get(url)

        source = url_a.content
        soup = BeautifulSoup(source,'html.parser')

        Tag = soup.find_all('meta', {'property':'og:image'})
        img = Tag[0]['content']

        d = str(datetime.datetime.now().time())

        urllib.request.urlretrieve(img,"InstaImg" + d[6:8] + ".jpg")

        self.label_3.setText("Download Completed")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
