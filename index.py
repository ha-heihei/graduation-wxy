from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from window import UI_Index

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox
import requests
import threading
import time
import os
import encryption_util as enUtil
from threading import Thread

from websearch import getAllUrl
import re

import w8ay
from w8ay import main

comp = re.compile(
    "((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?")



class IndexWindow(QMainWindow, UI_Index):

    leakScanFileName=''

    def __init__(self):
        super(IndexWindow, self).__init__()
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)
        self.submit.clicked.connect(lambda: self.submitEvent())
        self.submitAttack.clicked.connect(lambda: self.webAttackEvent())
        self.otherEncryptionBtn.clicked.connect(lambda: self.otherEncrytEvent())  # 其他加密
        self.symEncryptionBtn.clicked.connect(lambda: self.symEncrytEvent())  # 对称加密
        self.symDecipherBtn.clicked.connect(lambda: self.symDecipherEvent())
        self.asymEncryptionBtn.clicked.connect(lambda: self.asymEncrytEvent())  # 非对称加密
        self.asymDecipherBtn.clicked.connect(lambda: self.asymGetKey())

        # 漏洞扫描
        self.leakScanBtn.clicked.connect(lambda : self.leakScanEvent())
        # 注入测试
        self.injectBtn.clicked.connect(lambda :self.injectEvent())


    def symDecipherEvent(self):
        key = self.symKey.toPlainText()
        text = self.symContent.toPlainText()
        type = self.symCombBox.currentText()
        if text.strip() == '':
            self.messageDialog("转换内容不能为空")
            return
        if key.strip() == '':
            self.messageDialog("密钥不能为空")
            return

        if type == "DES" and len(key.strip()) != 8:
            self.messageDialog("DES算法密钥长度必须为8位")
            return

        if type == "3DES" and (len(key.strip()) != 16 and len(key.strip()) != 24):
            self.messageDialog("3DES算法密钥长度必须为16位或24位")
            return
        rs = ''
        if type == 'DES':
            rs = enUtil.DESDecryption(text, key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        elif type == 'AES':
            rs = enUtil.AES_decrypt(text, key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        else:
            des3 = enUtil.DES3Encryt(key)
            rs = des3.decrypt(text)
            if rs is None:
                self.messageDialog("转换失败")
                return
        self.symResult.setPlainText(rs)

    def asymGetKey(self):
        privateKey, publicKey = enUtil.get_rsa_key()
        self.asymPrivateKey.setPlainText(str(privateKey.decode()))
        self.asymPublicKey.setPlainText(str(publicKey.decode()))

    def asymEncrytEvent(self):
        text = self.asymContent.toPlainText()
        if text.strip() == '':
            self.messageDialog("转换内容不能为空")
            return
        type = self.asymCombBox.currentText()
        rs = ''
        publicKey = self.asymPublicKey.toPlainText()
        if publicKey.strip() == '':
            self.messageDialog("公钥不能为空，请先生成公钥")
            return
        if type == 'RSA':
            rs = enUtil.RSAEncryt(text, publicKey)
            if rs is None:
                self.messageDialog("转换失败")
                return
        else:
            self.messageDialog(f"{type}算法暂未开放")
            return
        self.asymResult.setPlainText(rs)

    def symEncrytEvent(self):
        key = self.symKey.toPlainText()
        text = self.symContent.toPlainText()
        type = self.symCombBox.currentText()
        if text.strip() == '':
            self.messageDialog("转换内容不能为空")
            return
        if key.strip() == '':
            self.messageDialog("密钥不能为空")
            return

        if type == "DES" and len(key.strip()) != 8:
            self.messageDialog("DES算法密钥长度必须为8位")
            return

        if type == "3DES" and (len(key.strip()) != 16 and len(key.strip()) != 24):
            self.messageDialog("3DES算法密钥长度必须为16位或24位")
            return
        rs = ''
        if type == 'DES':
            rs = enUtil.DESEncrytion(text, key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        elif type == 'AES':
            rs = enUtil.AES_encrypt(text, key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        else:
            des3 = enUtil.DES3Encryt(key)
            rs = des3.encrypt(text)
            if rs is None:
                self.messageDialog("转换失败")
                return
        self.symResult.setPlainText(rs)

    def otherEncrytEvent(self):
        text = self.otherContent.toPlainText()
        if text.strip() == '':
            self.messageDialog("加密内容不能为空")
            return
        type = self.otherCombBox.currentText()
        rs = ''
        if type == 'MD5':
            rs = enUtil.MD5Encrytion(text)
        elif type == 'SHA1':
            rs = enUtil.SHA1Encrytion(text)
        else:
            rs = enUtil.Base64Encrythion(text)
        self.otherResult.setPlainText(rs)

    def outputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def submitEvent(self):
        url = self.webUrl.text()
        if not comp.search(url):
            self.messageDialog("请输入正确的url")
            return
        urls = getAllUrl(url)
        if len(urls) == 0:
            self.messageDialog("解析链接为空")
            return
        self.tableShow([(item["url"], item["type"]) for item in urls])

    def tableShow(self, urls):
        self.model = QStandardItemModel(len(urls), 2)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['url', '来源'])  # 设置每列标题
        for row in range(len(urls)):
            for column in range(2):
                item = QStandardItem(urls[row][column])  # 创建模板内容
                self.model.setItem(row, column, item)  # 向模板里添加 item
        self.tableView.setModel(self.model)  # 表格设置模板
        self.tableView.clicked.connect(self.tableClickEvent)

    def tableClickEvent(self, index):
        text = self.model.item(index.row(), 0).text()
        self.webView.setUrl(QUrl(text))

    def messageDialog(self, msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
        msg_box.exec_()

    #################################网站攻击####################################
    def webAttackEvent(self):
        url = self.webUrlAttack.text()
        threadNum = self.webUrlAttackThreadNum.text()
        if not comp.search(url):
            self.messageDialog("请输入正确的url")
            return
        try:
            threadNum = int(threadNum)
            if threadNum < 1 or threadNum > 64:
                self.messageDialog("线程数在1到64之间")
                return
        except:
            self.messageDialog("请输入正确的线程数")
            return

        filename = time.strftime("%Y_%m_%d_%H_%M_%S")
        open("data/attack_log/" + filename + ".txt", 'w').close()
        self.textEdit.append(f"日志文件保存在data/attack_log/{filename}.txt文件中\n\n")
        sys.stdout = EmittingStr(textWritten=self.outputWritten)  # 开启GUI输出
        for i in range(threadNum):
            threading.Thread(target=self.threadAttack, args=(url, filename)).start()

    def threadAttack(self, url, filename):
        for i in range(10):
            res = requests.get(url)
            data = f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{threading.currentThread().getName()}的第{i + 1}次请求攻击\t{res.status_code}\t{url}"
            self.saveLog(filename, data)

    def saveLog(self, filename, data):
        lock = threading.Lock()
        lock.acquire()
        # self.textEdit.append(f"\n\n{data}")
        print(data)
        with open("data/attack_log/" + filename + ".txt", "a", encoding="utf-8") as f:
            f.write(data + "\n")
        lock.release()

    # 重定向到漏洞扫描输出台
    def redirectLeakScanOutput(self,text):
        if len(self.leakScanFileName)>0:
            with open("data/leak_scan/" + self.leakScanFileName + ".txt", "a", encoding="utf-8") as f:
                f.write(text)
        cursor = self.leakScanConsole.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.leakScanConsole.setTextCursor(cursor)
        self.leakScanConsole.ensureCursorVisible()

    def leakScanEvent(self):
        leakScanUrl=self.leakScanUrl.text()
        if not comp.search(leakScanUrl):
            self.messageDialog("请输入正确的url")
            return
        sys.stdout = EmittingStr(textWritten=self.redirectLeakScanOutput)  # 开启GUI输出
        self.leakScanFileName=time.strftime("%Y_%m_%d_%H_%M_%S")
        open("data/leak_scan/" + self.leakScanFileName + ".txt", 'w').close()
        scanThread=Thread(target=main,args=(leakScanUrl,))
        scanThread.daemon=True
        scanThread.start()
        self.leakScanStopBtn.clicked.connect(lambda: self.stopLeakScan(scanThread))

    def stopLeakScan(self,t):
        if t!=None and t.isAlive():
            w8ay.stop_thread(t)
            self.messageDialog("扫描已成功关闭")
        else:
            self.messageDialog("扫描未开启")


    # 注入测试脚本
    def injectEvent(self):
        pass
    # TODO 完成sql注入脚本






class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
    def write(self, text):
        self.textWritten.emit(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = IndexWindow()
    w.show()
    sys.exit(app.exec_())