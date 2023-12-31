# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_No = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_No.sizePolicy().hasHeightForWidth())
        self.pushButton_No.setSizePolicy(sizePolicy)
        self.pushButton_No.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_No.setObjectName("pushButton_No")
        self.gridLayout_2.addWidget(self.pushButton_No, 1, 2, 1, 1)
        self.integralView = QtWidgets.QGraphicsView(self.widget)
        self.integralView.setMinimumSize(QtCore.QSize(900, 600))
        self.integralView.setObjectName("integralView")
        self.gridLayout_2.addWidget(self.integralView, 0, 0, 9, 2)
        self.pushButton_Next = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Next.sizePolicy().hasHeightForWidth())
        self.pushButton_Next.setSizePolicy(sizePolicy)
        self.pushButton_Next.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_Next.setObjectName("pushButton_Next")
        self.gridLayout_2.addWidget(self.pushButton_Next, 3, 2, 1, 1)
        self.pushButton_Yes = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Yes.sizePolicy().hasHeightForWidth())
        self.pushButton_Yes.setSizePolicy(sizePolicy)
        self.pushButton_Yes.setMinimumSize(QtCore.QSize(2, 0))
        self.pushButton_Yes.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_Yes.setObjectName("pushButton_Yes")
        self.gridLayout_2.addWidget(self.pushButton_Yes, 0, 2, 1, 1)
        self.pushButton_Uncertain = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Uncertain.sizePolicy().hasHeightForWidth())
        self.pushButton_Uncertain.setSizePolicy(sizePolicy)
        self.pushButton_Uncertain.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_Uncertain.setObjectName("pushButton_Uncertain")
        self.gridLayout_2.addWidget(self.pushButton_Uncertain, 2, 2, 1, 1)
        self.textEdit_info = QtWidgets.QTextEdit(self.widget)
        self.textEdit_info.setMaximumSize(QtCore.QSize(100, 200))
        self.textEdit_info.setObjectName("textEdit_info")
        self.gridLayout_2.addWidget(self.textEdit_info, 6, 2, 1, 1)
        self.pushButton_Last = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Last.sizePolicy().hasHeightForWidth())
        self.pushButton_Last.setSizePolicy(sizePolicy)
        self.pushButton_Last.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_Last.setObjectName("pushButton_Last")
        self.gridLayout_2.addWidget(self.pushButton_Last, 4, 2, 1, 1)
        self.pushButton_NextFolder = QtWidgets.QPushButton(self.widget)
        self.pushButton_NextFolder.setEnabled(True)
        self.pushButton_NextFolder.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_NextFolder.setObjectName("pushButton_NextFolder")
        self.gridLayout_2.addWidget(self.pushButton_NextFolder, 7, 2, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSever = QtWidgets.QMenu(self.menubar)
        self.menuSever.setObjectName("menuSever")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Floder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Floder.setObjectName("actionOpen_Floder")
        self.actionOpen_Folders = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folders.setObjectName("actionOpen_Folders")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.menuFile.addAction(self.actionOpen_Floder)
        self.menuFile.addAction(self.actionOpen_Folders)
        self.menuSever.addAction(self.actionLogin)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSever.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_No.setText(_translate("MainWindow", "No"))
        self.pushButton_Next.setText(_translate("MainWindow", "Next"))
        self.pushButton_Yes.setText(_translate("MainWindow", "Yes"))
        self.pushButton_Uncertain.setText(_translate("MainWindow", "Uncertain"))
        self.pushButton_Last.setText(_translate("MainWindow", "Last"))
        self.pushButton_NextFolder.setText(_translate("MainWindow", "Next Folder"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSever.setTitle(_translate("MainWindow", "Server"))
        self.actionOpen_Floder.setText(_translate("MainWindow", "Open Folder"))
        self.actionOpen_Folders.setText(_translate("MainWindow", "Open Folders"))
        self.actionLogin.setText(_translate("MainWindow", "Login and Upload"))
        self.actionUpload.setText(_translate("MainWindow", "Upload"))
