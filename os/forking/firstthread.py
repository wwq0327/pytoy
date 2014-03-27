#!/usr/bin/env python

import sys
import threading
import time

def sleepandprint():
    time.sleep(1)
    print 'Hello from both of us.'

def threadcode():
    sys.stdout.write("Hello from the new thread. My name is %s\n" %
                 threading.currentThread().getName())
    sleepandprint()

print "Before starting a new thread, my name is", \
      threading.currentThread().getName()

# Create new thread
t = threading.Thread(target=threadcode, name="ChildThread")

# This thread won't keep the program from terminating.
t.setDaemon(1)

# Start the new thread
t.start()
sys.stdout.write("Hello from the main thread. My name is %s\n" %
             threading.currentThread().getName())
sleepandprint()

# Wait for the child thread to exit.
t.join()
