# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Development\smalltools\Python\CompareData\ui\Formatter.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from utils import Files


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 112)
        self.verticalWidget = QtWidgets.QWidget(MainWindow)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.upload_btn = QtWidgets.QPushButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.upload_btn.setFont(font)
        self.upload_btn.setObjectName("upload_btn")
        self.verticalLayout.addWidget(self.upload_btn)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.exec_btn = QtWidgets.QPushButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exec_btn.setFont(font)
        self.exec_btn.setObjectName("exec_btn")
        self.verticalLayout.addWidget(self.exec_btn)
        MainWindow.setCentralWidget(self.verticalWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.upload_btn.clicked.connect(self.upload_btn_clicked)

    def upload_btn_clicked(self):
        self.filepath = Files.openfile()
        print('abc')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "重组表格工具 V1.0.0 From 郑人滏"))
        self.label_1.setText(_translate("MainWindow", "上传"))
        self.upload_btn.setText(_translate("MainWindow", "上传文件"))
        self.label_2.setText(_translate("MainWindow", "输出"))
        self.exec_btn.setText(_translate("MainWindow", "执行任务"))