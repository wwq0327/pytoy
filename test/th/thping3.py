#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from subprocess import call, STDOUT
import time

ips = '192.168.1.'

def ping(ip):
    ip = str(ip)
    cmd = 'ping -c 1 ' + ips + ip
    ret = call(cmd, shell=True, stdout=open('/dev/null', 'w'), stderr=STDOUT)
    if ret == 0:
        print '找有到有效ip: %s' % (ips+ip)
        time.sleep(1)

def main():
    threads = []
    for i in range(1, 255):
        t = threading.Thread(target=ping, args=(i, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
    
