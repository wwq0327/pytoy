#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-08 12:56:48

import subprocess

def pinger(ip):
    p = subprocess.call('ping -c 1 %s'%ip,
            shell=True, 
            stdout=open('/dev/null', 'w')
            )
    return p

def th_ping():
    ip_list = []
    for end in xrange(100, 150):
        ip = '192.168.1.%s' % end
        p = pinger(ip)
        if p == 0:
            ip_list.append(ip)
            print '正在使用的IP ==> %s ***' % ip
        else:
            print '未被使用的IP ==> %s' % ip

    return ip_list

def main():
    for i in th_ping():
        print i

if __name__ == '__main__':
    main()
