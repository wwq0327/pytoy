#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import subprocess

urls = ['http://www.baidu.com',
        'http://bing.com',
        'http://python.org']
cmd = 'ping -c 4 %s'

def ping(url):
    ps = subprocess.Popen(cmd%url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out_lines = ps.stdout.readlines()
    for s in out_lines:
        print s

def main():
    threads = []
    nloops = range(len(urls))
    for i in nloops:
        t = threading.Thread(target=ping, args=(urls[i],))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

def test():
    for url in urls:
        ping(url)

if __name__ == '__main__':
    test()
