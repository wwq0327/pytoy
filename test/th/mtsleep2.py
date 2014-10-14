#!/usr/bin/env python
import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()

def main():
    print 'starting at:', ctime()
    locks = [] ## 锁队列
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire() # 获得锁
        locks.append(lock)
    # 执行进程
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # 遍历锁，当队列中的所有锁都解开时，才开始运行下一步
    for i in nloops:
        while locks[i].locked():pass

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
