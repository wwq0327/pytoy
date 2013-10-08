#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-08 13:16:20

import subprocess
from threading import Thread
from Queue import Queue

num_threads = 5 
queue = Queue()

def gen_ips():
    ips = []
    for num in xrange(100, 120):
        ip = '192.168.1.%s' % num
        ips.append(ip)
    return ips

def pinger(q):
    while True:
        ip = q.get() # 接收执行参数
        ret = subprocess.call('ping -c 1 %s' % ip,
                shell=True,
                stdout=open('/dev/null', 'w'),
                stderr=subprocess.STDOUT)
        if ret == 0:
            print '正在使用的IP ==> %s ***' % ip
        else:
            print '未被使用的IP ==> %s' % ip

        q.task_done()
def run():
    # 线程设置
    for i in range(num_threads):
        worker = Thread(target=pinger, args=(queue,))
        worker.setDaemon(True)
        worker.start()

    for ip in gen_ips():
        queue.put(ip) # 放执行的参数

    print "Main Thread Waiting"
    queue.join() # 开始执行
    print "Done"

if __name__ == '__main__':
    run()
