# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(565, 336)
        self.label = QtWidgets.QLabel(Server)
        self.label.setGeometry(QtCore.QRect(50, 40, 61, 31))
        self.label.setObjectName("label")
        self.lineEdit_host = QtWidgets.QLineEdit(Server)
        self.lineEdit_host.setGeometry(QtCore.QRect(102, 40, 161, 31))
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.lineEdit_port = QtWidgets.QLineEdit(Server)
        self.lineEdit_port.setGeometry(QtCore.QRect(352, 40, 81, 31))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.label_2 = QtWidgets.QLabel(Server)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 81, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_user = QtWidgets.QLineEdit(Server)
        self.lineEdit_user.setGeometry(QtCore.QRect(102, 100, 161, 31))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.label_3 = QtWidgets.QLabel(Server)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Server)
        self.label_4.setGeometry(QtCore.QRect(278, 100, 81, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_password = QtWidgets.QLineEdit(Server)
        self.lineEdit_password.setGeometry(QtCore.QRect(350, 100, 161, 31))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_5 = QtWidgets.QLabel(Server)
        self.label_5.setGeometry(QtCore.QRect(48, 160, 61, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_local = QtWidgets.QLineEdit(Server)
        self.lineEdit_local.setGeometry(QtCore.QRect(100, 160, 241, 31))
        self.lineEdit_local.setObjectName("lineEdit_local")
        self.pushButton_Select = QtWidgets.QPushButton(Server)
        self.pushButton_Select.setGeometry(QtCore.QRect(380, 160, 93, 31))
        self.pushButton_Select.setObjectName("pushButton_Select")
        self.lineEdit_server = QtWidgets.QLineEdit(Server)
        self.lineEdit_server.setGeometry(QtCore.QRect(102, 220, 241, 31))
        self.lineEdit_server.setObjectName("lineEdit_server")
        self.label_6 = QtWidgets.QLabel(Server)
        self.label_6.setGeometry(QtCore.QRect(50, 220, 61, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton_upload = QtWidgets.QPushButton(Server)
        self.pushButton_upload.setGeometry(QtCore.QRect(220, 270, 111, 41))
        self.pushButton_upload.setObjectName("pushButton_upload")

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Form"))
        self.label.setText(_translate("Server", "Host"))
        self.label_2.setText(_translate("Server", "Port"))
        self.label_3.setText(_translate("Server", "User"))
        self.label_4.setText(_translate("Server", "Password"))
        self.label_5.setText(_translate("Server", "Local"))
        self.pushButton_Select.setText(_translate("Server", "Select"))
        self.label_6.setText(_translate("Server", "Server"))
        self.pushButton_upload.setText(_translate("Server", "Upload"))
