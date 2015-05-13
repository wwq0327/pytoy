#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import threading

urls = ['http://www.baidu.com',
        'http://weibo.com',
        'http://bing.com',
        'http://joinwee.com']

class WorkThread(threading.Thread):
    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        apply(self.func, self.args)

def getinfo(url):
    req = urllib2.urlopen(url)
    print req.info()

def main():
    threads = []
    for i in range(len(urls)):
        t = WorkThread(getinfo, (urls[i],))
        t.setDaemon(1)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
