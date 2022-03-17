# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit
import hashlib
from dbutil import DBUtil
import datetime


class RegisterUI(object):
    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("Register")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 91, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 130, 241, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setObjectName("userName")
        self.verticalLayout_3.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setObjectName("userPwd")
        self.verticalLayout_3.addWidget(self.password)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(13, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.secretQuestionSpin = QtWidgets.QComboBox(self.widget)
        self.secretQuestionSpin.setObjectName("secretQuestionSpin")
        self.secretQuestionSpin.addItem("")
        self.secretQuestionSpin.addItem("")
        self.secretQuestionSpin.addItem("")
        self.verticalLayout.addWidget(self.secretQuestionSpin)
        self.secretQuestionAnswer = QtWidgets.QLineEdit(self.widget)
        self.secretQuestionAnswer.setObjectName("secretQuestionAnswer")
        self.verticalLayout.addWidget(self.secretQuestionAnswer)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.registerBtn = QtWidgets.QPushButton(self.widget)
        self.registerBtn.setObjectName("registerBtn")
        self.verticalLayout_5.addWidget(self.registerBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        self.bindEvent()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label_3.setText(_translate("MainWindow", "注册"))
        # self.label.setText(_translate("MainWindow", "用户名"))
        # self.label_2.setText(_translate("MainWindow", "密码"))
        # self.registerBtn.setText(_translate("MainWindow", "注册"))
        # MainWindow.setWindowTitle(_translate("Register", "注册"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">注册</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "用户名"))
        self.label_3.setText(_translate("MainWindow", "密码"))
        self.label_4.setText(_translate("MainWindow", "密保问题"))
        self.secretQuestionSpin.setItemText(0, _translate("MainWindow", "你的学校名称？"))
        self.secretQuestionSpin.setItemText(1, _translate("MainWindow", "你的父亲名称？"))
        self.secretQuestionSpin.setItemText(2, _translate("MainWindow", "你的宠物名称？"))
        self.registerBtn.setText(_translate("MainWindow", "注册"))

    def bindEvent(self,):
        self.registerBtn.clicked.connect(lambda:self.registerEvent())

    def registerEvent(self):
        username = self.username.text()
        password = self.password.text()

        index = self.secretQuestionSpin.currentIndex()
        secretQuestion = self.secretQuestionSpin.itemText(index)
        secretAnswer=self.secretQuestionAnswer.text()

        if username.strip() == '' or password.strip() == '':
            self.messageDialog("用户名或密码不能为空")
            return
        if len(secretAnswer)<=0:
            self.messageDialog("密保答案为空")
            return
        # password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        nowTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into user(username,password,secret_question,secret_answer,create_time) values(%s,%s,%s,%s,%s)"
        db = DBUtil()
        if db.update(sql, values=(username, password,secretQuestion,secretAnswer,nowTime)):
            self.messageDialog("注册成功")
            db.close()
        else:
            self.messageDialog("注册失败")

    def messageDialog(self, msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
        msg_box.exec_()

