#!/usr/bin/env python
'''
Standard Producer/Consumer Threading Pattern
'''
import time
import threading
import Queue
import urllib2

urls = [
        'http://python.org',
        'http://www.yahoo.com',
        'http://weibo.com',
        'http://baidu.com'
        ]

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._q = queue

    def run(self):
        while 1:
            content = self._q.get()
            if isinstance(content, str) and content == 'quit':
                break
            #print "I'm a thread, and I received %s!!" % msg

            response = urllib2.urlopen(content)
        print "Bye byes!"

def producer():
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, 4)
    start_time = time.time()

    for url in urls:
        queue.put(url)
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()

    print 'Done! Time taken: {}'.format(time.time() - start_time)

def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers

if __name__ == '__main__':
    producer()
