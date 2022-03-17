#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:w8ayScan
Author:w8ay
Copyright (c) 2017
'''
import sys
from imp import reload

from lib.core.Spider import SpiderMain
from lib.core import webcms,PortScan,common,webdir,fun_until
from lib.core import outputer

from threading import Thread
import ctypes
import inspect

import time

reload(sys)
# sys.setdefaultencoding('utf-8')
def main(url):
    root = url
    domain = common.w8urlparse(root)
    threadNum = 10
    output = outputer.outputer()
    # CDN Check
    # print("CDN check....")
    iscdn = True
    # try:
    #     msg,iscdn =  fun_until.checkCDN(root)
    #     output.add("cdn",msg)
    #     output.build_html(domain)
    #     print(msg)
    # except:
    #     print("[Error]:CDN check error")

    if iscdn:
        #IP Ports Scan
        ip = common.gethostbyname(root)
        print("IP:",ip)
        print("START Port Scan:")
        pp = PortScan.PortScan(ip)
        pp.work()
        output.build_html(domain)
    
    # DIR Fuzz
    dd = webdir.webdir(root,threadNum)    
    dd.work()
    dd.output()
    output.build_html(domain)
    #webcms
    ww = webcms.webcms(root,threadNum)
    ww.run()
    output.build_html(domain)
    #spider
    w8 = SpiderMain(root,threadNum)
    w8.craw()


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    """
    @profile:强制停掉线程函数
    :param thread:
    :return:
    """
    if thread == None:
        print('thread id is None, return....')
        return
    _async_raise(thread.ident, SystemExit)


if __name__ == '__main__':
    t=Thread(target=main)
    t.start()
    time.sleep(3)
    stop_thread(t)