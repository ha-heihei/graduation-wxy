# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backSecret.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class BackSecretUI(object):
    def setupUi(self, forgetSecret):
        forgetSecret.setObjectName("forgetSecret")
        forgetSecret.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(forgetSecret)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 60, 161, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 130, 301, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.secretQuestion = QtWidgets.QLineEdit(self.widget)
        self.secretQuestion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.secretQuestion.setObjectName("secretQuestion")
        self.horizontalLayout.addWidget(self.secretQuestion)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.secretAnswer = QtWidgets.QLineEdit(self.widget)
        self.secretAnswer.setObjectName("secretAnswer")
        self.horizontalLayout_2.addWidget(self.secretAnswer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.selfSecret = QtWidgets.QLineEdit(self.widget)
        self.selfSecret.setObjectName("selfSecret")
        self.horizontalLayout_3.addWidget(self.selfSecret)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.backSecretBtn = QtWidgets.QPushButton(self.widget)
        self.backSecretBtn.setObjectName("backSecretBtn")
        self.verticalLayout_3.addWidget(self.backSecretBtn)
        forgetSecret.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(forgetSecret)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        forgetSecret.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(forgetSecret)
        self.statusbar.setObjectName("statusbar")
        forgetSecret.setStatusBar(self.statusbar)

        self.retranslateUi(forgetSecret)
        QtCore.QMetaObject.connectSlotsByName(forgetSecret)

    def retranslateUi(self, forgetSecret):
        _translate = QtCore.QCoreApplication.translate
        forgetSecret.setWindowTitle(_translate("forgetSecret", "找回密码"))
        self.label.setText(_translate("forgetSecret", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">找回密码</span></p></body></html>"))
        self.label_2.setText(_translate("forgetSecret", "密保问题"))
        self.label_3.setText(_translate("forgetSecret", "密保答案"))
        self.label_4.setText(_translate("forgetSecret", "您的密码"))
        self.backSecretBtn.setText(_translate("forgetSecret", "确认"))

