import sys

from PyQt5.QtCore import Qt

from UI.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPixmap, QPainter
import pandas as pd
import numpy as np
from server import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.userName = None
        self.csvPath = None

    def init_ui(self):
        self.setupUi(self)
        self.xlsxName = None  # excel路径
        self.labelDict = {}  # 已经打标签的数据
        self.index_1 = 0  # 当前打标签的索引
        self.colIndex = 2
        self.flag = True  # 用于判断是否认证完成
        self.actionOpen_Floder.triggered.connect(lambda: self.OpenFolder1(folderspath=None))
        self.actionOpen_Folders.triggered.connect(self.OpenFolders)
        self.pushButton_NextFolder.clicked.connect(self.NextFolder)
        self.pushButton_Yes.clicked.connect(lambda: self.MakeTag(label='Yes'))
        self.pushButton_No.clicked.connect(lambda: self.MakeTag(label='No'))
        self.pushButton_Uncertain.clicked.connect(lambda: self.MakeTag(label='Uncertain'))
        self.pushButton_Next.clicked.connect(self.NextData)
        self.pushButton_Last.clicked.connect(self.LastData)
        self.actionLogin.triggered.connect(self.LoginServer)
        # shuang
        self.len = 0
        self.folderPath = None
        self.pathName = None
        self.scene = QGraphicsScene()


    def OpenFolders(self):
        try:
            self.foldersPath = QFileDialog.getExistingDirectory(None, '选择文件夹')
            self.files = os.listdir(self.foldersPath)
        except Exception as e:
            print(e)
        self.pushButton_NextFolder.setEnabled(True)
        foldersPath = os.path.join(self.foldersPath, self.files[0])
        self.csvName = self.files[0] + '_' + self.userName + '.csv'
        self.files.remove(self.files[0])
        self.OpenFolder1(folderspath=foldersPath)

    def NextFolder(self):
        foldersPath = os.path.join(self.foldersPath, self.files[0])
        self.csvName = self.files[0] + '_' + self.userName + '.csv'
        self.files.remove(self.files[0])
        if len(self.files) == 0:
            self.pushButton_NextFolder.setEnabled(False)
        self.OpenFolder1(folderspath=foldersPath)
        print(len(self.files))

    def OpenFolder1(self, folderspath=None):
        try:
            if folderspath is None:
                self.folderPath = QFileDialog.getExistingDirectory(None, '选择文件夹')
                self.csvName = self.folderPath.split('/')[-1] + '_' + self.userName + '.csv'
                file = os.listdir(self.folderPath)
                self.pushButton_NextFolder.setEnabled(False)
            else:
                self.folderPath = folderspath
                file = os.listdir(self.folderPath)
            temp = []
            for item in file:
                if item.endswith('png'):
                    temp.append(item)
            file = temp
            if len(file) == 0:
                QMessageBox.information(self, 'Info',
                                        '{} Folder is None!'.format(self.csvName[: len(self.csvName) - 8]))
                if self.pushButton_NextFolder.isEnabled():
                    self.init_ui()
            else:
                allCsvName = os.listdir(self.csvPath)
                if self.csvName not in allCsvName:
                    df = pd.DataFrame(columns=['Name', 'Label'])
                    df.to_csv(os.path.join(self.csvPath, self.csvName), index=False, sep='\t',
                              encoding='utf-8')
                self.xlsxName = os.path.join(self.csvPath, self.csvName)
                self.fileName = [os.path.splitext(i)[0] for i in file]
                haveLabel = np.array(pd.read_csv(self.xlsxName, usecols=['Name'], sep='\t')).flatten()
                self.index = haveLabel.shape[0]  # excel表中已有的数据量
                for item in haveLabel:
                    self.fileName.remove(item)
                self.pathName = [i + '.png' for i in self.fileName]
                self.len = len(self.pathName)
                if len(self.fileName) == 0:
                    QApplication.setQuitOnLastWindowClosed(False)
                    QMessageBox.information(self, 'Info', 'All data has been authenticated!')
                    if self.pushButton_NextFolder.isEnabled():
                        self.init_ui()
                else:
                    self.ShowPic()
        except Exception as e:
            print(e)

    # def ShowPic(self):
    #     if self.index_1 == 0:
    #         self.pushButton_Last.setEnabled(False)
    #     else:
    #         self.pushButton_Last.setEnabled(True)
    #     if self.index_1 == self.len - 1:
    #         self.pushButton_Next.setEnabled(False)
    #     else:
    #         self.pushButton_Next.setEnabled(True)
    #     img1 = QPixmap()
    #     img1.load(os.path.join(self.folderPath, self.pathName[self.index_1]))
    #     self.item = QGraphicsPixmapItem(img1)
    #     self.sence = QGraphicsScene()
    #     self.sence.addItem(self.item)
    #     self.integralView.setScene(self.sence)
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.ShowPic()

    def ShowPic(self):
        if not self.folderPath:
            return
        if self.index_1 == 0:
            self.pushButton_Last.setEnabled(False)
        else:
            self.pushButton_Last.setEnabled(True)
        if self.index_1 == self.len - 1:
            self.pushButton_Next.setEnabled(False)
        else:
            self.pushButton_Next.setEnabled(True)

        img1 = QPixmap()
        img1.load(os.path.join(self.folderPath, self.pathName[self.index_1]))

        # 设置场景
        if not hasattr(self, 'sence'):
            self.sence = QGraphicsScene()
            self.integralView.setScene(self.sence)
        else:
            self.sence.clear()  # 清空场景

        # 创建图像项并将其添加到场景
        self.item = QGraphicsPixmapItem(img1)
        self.sence.addItem(self.item)

        # 获取integralView的大小
        view_rect = self.integralView.viewport().rect()

        # 获取图像的原始大小
        img_rect = img1.rect()

        # 计算图像的缩放比例
        scale_factor = min(view_rect.width() / img_rect.width(), view_rect.height() / img_rect.height())

        # 缩放图像
        self.item.setScale(scale_factor)

        # 居中图像
        self.integralView.setSceneRect(self.sence.sceneRect())
        self.integralView.centerOn(self.item)



    def MakeTag(self, label):
        df = pd.read_csv(self.xlsxName, encoding='utf-8', sep='\t')
        if self.fileName[self.index_1] in self.labelDict.keys():
            df['Label'].loc[self.labelDict[self.fileName[self.index_1]]] = '{}'.format(label)
        else:
            df = df.append(pd.Series({'Name': self.fileName[self.index_1], 'Label': '{}'.format(label)}),
                           ignore_index=True)
            self.labelDict[self.fileName[self.index_1]] = self.index
            self.index += 1
        if self.flag is True:  # 用于认证完成之后窗口异常弹出
            self.initIndex = self.index - 1
            self.flag = False
        self.textEdit_info.setPlainText(
            'Information:\nName:{};\nLabel:{}.'.format(self.fileName[self.index_1], label))
        df.to_csv(self.xlsxName, encoding='utf-8', index=False, sep='\t')
        if self.index != (self.len + self.initIndex):
            self.NextData()
        else:
            QMessageBox.warning(self, 'WARNING', 'task is over!')
            self.init_ui()

    def NextData(self):
        self.index_1 += 1
        self.ShowPic()

    def LastData(self):
        self.index_1 -= 1
        self.ShowPic()

    def _compalte(self):
        self.setupUi(self)

    def LoginServer(self):
        self.serverWindow = Server()
        self.serverWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
