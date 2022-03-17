from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

import sys

from backSecret import BackSecretUI
from dbutil import DBUtil


class BackSecretWindow(QMainWindow, BackSecretUI):

    def __init__(self,userName):
        super(BackSecretWindow, self).__init__()
        self.setupUi(self)

        self.queryQuestion(userName)

        self.backSecretBtn.clicked.connect(lambda :self.queryPwd(userName))

    def queryQuestion(self,userName):
        db=DBUtil()
        sql="select * from user where username=%s"
        rs=db.query(sql,(userName))[0]
        self.secretQuestion.setText(rs["secret_question"])
        # self.secretAnswer.setText(rs["secret_answer"])
        db.close()

    def queryPwd(self,userName):
        secretQuestion=self.secretQuestion.text()
        secretAnswer=self.secretAnswer.text()
        if len(secretAnswer)<=0:
            self.messageDialog("未输入密保问题")
            return
        db=DBUtil()
        sql="select * from user where username=%s and secret_question=%s and secret_answer=%s"
        rs=db.query(sql,(userName,secretQuestion,secretAnswer))[0]
        self.selfSecret.setText(rs["password"])
        db.close()

    def messageDialog(self,msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BackSecretWindow("")
    w.show()
    sys.exit(app.exec_())
