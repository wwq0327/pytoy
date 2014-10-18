#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from subprocess import call
import time

ips = '192.168.1.'

def ping(ip):
    ip = str(ip)
    ret = call(['ping', '-c 1', ip], shell=True)
    if ret != 0:
        print '无效的ip: %s' % (ips+ip)
    print '找有到有交ip: %s' % (ips+ip)
    time.sleep(1)

def main():
    threads = []
    for i in range(1, 255):
        t = threading.Thread(target=ping, args=(i, ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
    
