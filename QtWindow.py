# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textt = QtWidgets.QTextEdit(self.centralwidget)
        self.textt.setGeometry(QtCore.QRect(250, 40, 256, 41))
        self.textt.setObjectName("text")
        self.textt.setEnabled(True)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(50, 40, 121, 31))
        self.btn.setAutoDefault(False)
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.accept)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFirstWindown = QtWidgets.QMenu(self.menubar)
        self.menuFirstWindown.setObjectName("menuFirstWindown")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.menubar.addAction(self.menuFirstWindown.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Display"))
        self.menuFirstWindown.setTitle(_translate("MainWindow", "menu"))
        self.menuEdit.setTitle(_translate("MainWindow", "edit"))
    def accept(self):
        self.textt.setPlainText('damnicomniplusvic')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
