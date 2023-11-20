from UI.server import Ui_Server
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
import paramiko
import os


class Server(Ui_Server, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sftp = None
        self.pushButton_Select.clicked.connect(self.SelectLocalFolder)
        self.pushButton_upload.clicked.connect(self.Login)

    def Login(self):
        host = self.lineEdit_host.text()
        port = int(self.lineEdit_port.text())
        user = self.lineEdit_user.text()
        password = self.lineEdit_password.text()
        try:
            self.transport = paramiko.Transport((host, port))
            self.transport.connect(username=user, password=password)
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        except:
            QMessageBox.information(self, 'Info', 'Server connection failure!')
        self.Upload()

    def Upload(self):
        localPath = self.lineEdit_local.text() + '/'
        serverPath = self.lineEdit_server.text()
        if serverPath[-1] != '/':
            serverPath = serverPath + '/'
        files = os.listdir(localPath)
        for item in files:
            localFilePath = os.path.join(localPath, item)
            serverFilePath = os.path.join(serverPath, item[: 10] + '/')
            self.sftp.put(localFilePath, os.path.join(serverFilePath, item[len(item) - 7:]))
        self.transport.close()
        QMessageBox.information(self, 'Info', 'Upload to complete!')

    def SelectLocalFolder(self):
        f = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.lineEdit_local.setText(f)
