#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from aip import AipFace
Ak = 'TBPtvVXmPoAnSX4ljiTkrpji'
Sk = '2wRiOMvA1yEvY09GRm4v6fSvW9H0Kzcj'
Ai = '9647392'
aipFace = AipFace(Ai, Ak, Sk)
aipFace.setConnectionTimeoutInMillis(2000)
aipFace.setSocketTimeoutInMillis(60000)
options = {
    'max_face_num': 5,
    'face_fields': "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities"
}
# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choosePic1 = QtWidgets.QPushButton(self.centralwidget)
        self.choosePic1.setGeometry(QtCore.QRect(40, 30, 101, 31))
        self.choosePic1.setObjectName("choosePic1")
        self.choosePic1.clicked.connect(self.choosePicOne)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 80, 141, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.choosePic2 = QtWidgets.QPushButton(self.centralwidget)
        self.choosePic2.setGeometry(QtCore.QRect(40, 230, 101, 31))
        self.choosePic2.setObjectName("choosePic2")
        self.choosePic2.clicked.connect(self.choosePicTwo)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(30, 300, 141, 131))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.detect = QtWidgets.QPushButton(self.centralwidget)
        self.detect.setGeometry(QtCore.QRect(40, 460, 101, 31))
        self.detect.setObjectName("detect")
        self.detect.clicked.connect(self.detectAction)
        self.match = QtWidgets.QPushButton(self.centralwidget)
        self.match.setGeometry(QtCore.QRect(40, 530, 101, 31))
        self.match.setObjectName("match")
        self.match.clicked.connect(self.matchAction)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(190, 80, 541, 451))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(760, 90, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(760, 170, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 250, 54, 12))
        self.label_3.setObjectName("label_3")
        self.beauty = QtWidgets.QTextBrowser(self.centralwidget)
        self.beauty.setGeometry(QtCore.QRect(810, 80, 111, 31))
        self.beauty.setObjectName("beauty")
        self.age = QtWidgets.QTextBrowser(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(810, 160, 111, 31))
        self.age.setObjectName("age")
        self.gender = QtWidgets.QTextBrowser(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(810, 240, 111, 31))
        self.gender.setObjectName("gender")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(760, 460, 54, 12))
        self.label_4.setObjectName("label_4")
        self.score = QtWidgets.QTextBrowser(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(800, 450, 111, 31))
        self.score.setObjectName("score")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 23))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choosePic1.setText(_translate("MainWindow", "ChoosePicture"))
        self.choosePic2.setText(_translate("MainWindow", "ChoosePicture"))
        self.detect.setText(_translate("MainWindow", "Detect"))
        self.match.setText(_translate("MainWindow", "Match"))
        self.label.setText(_translate("MainWindow", "beauty:"))
        self.label_2.setText(_translate("MainWindow", "age:"))
        self.label_3.setText(_translate("MainWindow", "gender:"))
        self.label_4.setText(_translate("MainWindow", "score:"))

    def choosePicOne(self):
        open = QFileDialog()
        self.path1 = open.getOpenFileName()
        # self.path1 = open.getOpenFileNames()
        print(type(self.path1))
        print(self.path1)
        if self.path1[0] == '':
            return
        #self.path1 = open.getExistingDirectory()
        self.path1 = self.path1[0]
        print(self.path1)
        image = QImage()
        image.load(self.path1)
        sence = QGraphicsScene()
        sence.addPixmap(QPixmap.fromImage(image))
        self.graphicsView.setScene(sence)
        self.graphicsView_3.setScene(sence)
        x1, y1 = float(image.width()), float(image.height())
        x2, y2 = float(self.graphicsView.width()), float(self.graphicsView.height())
        x3, y3 = float(self.graphicsView_3.width()), float(self.graphicsView_3.height())
        if x1/y1 > x2/y2:
            self.graphicsView.scale(x2/x1*0.98, x2/x1*0.98)
        else:
            self.graphicsView.scale(y2/y1*0.98, y2/y1*0.98)
        if x1/y1 > x3/y3:
            self.graphicsView_3.scale(x3/x1*0.98, x3/x1*0.98)
        else:
            self.graphicsView_3.scale(y3/y1*0.98, y3/y1*0.98)

    def choosePicTwo(self):
        open = QFileDialog()
        self.path2 = open.getOpenFileName()
        # self.path2 = open.getOpenFileNames()
        print(type(self.path2))
        print(self.path2)
        if self.path2[0] == '':
            return
        #self.path2 = open.getExistingDirectory()
        self.path2 = self.path2[0]
        print(self.path2)
        image = QImage()
        image.load(self.path2)
        sence = QGraphicsScene()
        sence.addPixmap(QPixmap.fromImage(image))
        self.graphicsView_2.setScene(sence)
        x1, y1 = float(image.width()), float(image.height())
        x2, y2 = float(self.graphicsView_2.width()), float(self.graphicsView_2.height())
        if x1/y1 > x2/y2:
            self.graphicsView_2.scale(x2/x1*0.98, x2/x1*0.98)
        else:
            self.graphicsView_2.scale(y2/y1*0.98, y2/y1*0.98)

    def detectAction(self):
        if self.path1 == '':
            return
        path = self.path1
        response = aipFace.detect(get_file_content(path), options)
        print(response)
        if response['result_num'] == 0:
            return
        result = response['result'][0]
        self.beauty.setPlainText(str(result['beauty']))
        self.age.setPlainText(str(result['age']))
        self.gender.setPlainText(result['gender'])

    def matchAction(self):
        if self.path1 == '':
            return
        if self.path2 == '':
            return
        response = aipFace.match([
            get_file_content(self.path1),
            get_file_content(self.path2)
        ])
        print(response)
        if response['result_num'] == 0:
            return
        result = response['result'][0]
        self.score.setPlainText(str(result['score']))

def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
