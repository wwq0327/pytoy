#!/usr/bin/env python
'''
Standard Producer/Consumer Threading Pattern
'''
import time
import threading
import Queue

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._q = queue

    def run(self):
        while 1:
            msg = self._q.get()
            if isinstance(msg, str) and msg == 'quit':
                break
            print "I'm a thread, and I received %s!!" % msg

        print "Bye byes!"

def producer():
    queue = Queue.Queue()
    worker = Consumer(queue)
    worker.start()
    start_time = time.time()
    while time.time() - start_time < 5:
        queue.put('something at %s' % time.time())
        time.sleep(1)

    queue.put('quit')
    worker.join()

if __name__ == '__main__':
    producer()
