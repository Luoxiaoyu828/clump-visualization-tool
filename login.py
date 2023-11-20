from UI.Login import Ui_Form
from main import *
from PyQt5 import QtWidgets


class Login(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_Login.clicked.connect(self.UserName)
        self.pushButton_Save.clicked.connect(self.save)

    def UserName(self):
        userName = self.lineEdit_User.text()
        csvPath = self.lineEdit_Path.text()
        if len(userName) == 0:
            QMessageBox.information(self, 'Info', 'Please enter a user name!')
        elif len(userName) != 3:
            QMessageBox.information(self, 'Info', 'The length of username is wrong!')
        elif len(csvPath) == 0:
            QMessageBox.information(self, 'Info', 'Please select a path!')
        else:
            mainWindow.userName = userName
            mainWindow.csvPath = csvPath
            self.close()
            mainWindow.show()

    def save(self):
        f = QtWidgets.QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.lineEdit_Path.setText(f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = Login()
    mainWindow = MainWindow()
    loginWindow.show()
    app.exec_()


