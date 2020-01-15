# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

class MyClass(QtCore.QObject):

    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        print("按钮按下. slot on_clicked()")

    @QtCore.pyqtSlot(bool, name="myslot")
    def on_clicked2(self, status):
        print("按钮按下. slot myslot(bool)", status)

obj = MyClass()
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("点击鼠标")
button.clicked.connect(obj.on_clicked)
button.clicked.connect(obj.myslot)
button.show()
sys.exit(app.exec_()) 