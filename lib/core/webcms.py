#!/usr/bin/env python
# __author__= 'w8ay'
import json,os,sys,hashlib,threading
from queue import Queue
from lib.core import Download
from lib.core import outputer
output = outputer.outputer()

class webcms(object):
    workQueue = Queue()
    URL = ""
    threadNum = 0
    NotFound = True
    Downloader = Download.Downloader()
    result = ""

    def __init__(self,url,threadNum = 10):
        try:
            self.URL = url
            self.threadNum = threadNum
            filename = os.path.join(sys.path[0], "data", "data.json")
            fp = open(filename,encoding='utf8')
            webdata = json.load(fp)
            for i in webdata:
                self.workQueue.put(i)
            fp.close()
        except:
            print("webdata数据加载失败")

    def getmd5(self, body):
        m2 = hashlib.md5()
        m2.update(body.encode(encoding="utf-8"))
        return m2.hexdigest()

    def th_whatweb(self):
        if(self.workQueue.empty()):
            self.NotFound = False
            return False

        if(self.NotFound is False):
            return False
        cms = self.workQueue.get()
        _url = self.URL + cms["url"]
        html = self.Downloader.get(_url)
        print("[whatweb log]:checking %s"%_url)
        if(html is None):
            return False
        if cms["re"]:
            if(html.find(cms["re"])!=-1):
                self.result = cms["name"]
                self.NotFound = False
                return True
        else: 
            md5 = self.getmd5(html)
            if(md5==cms["md5"]):
                self.result = cms["name"]
                self.NotFound = False
                return True
    
    def run(self):
        while(self.NotFound):
            th = []
            for i in range(self.threadNum):
                t = threading.Thread(target=self.th_whatweb)
                t.start()
                th.append(t)
            for t in th:
                t.join()
        if(self.result):
            print("[webcms]:%s cms is %s"%(self.URL,self.result))
            output.add("Webcms","[webcms]:%s cms is %s"%(self.URL,self.result))
        else:
            print("[webcms]:%s cms NOTFound!"%self.URL)
            output.add("Webcms","[webcms]:%s cms NOTFound!"%self.URL)