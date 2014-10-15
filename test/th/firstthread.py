#!/usr/bin/env python
import threading, time
import sys

def sleepandprint():
    time.sleep(1)
    print "Hello from both of us."

def threadcode():
    sys.stdout.write("Hello from the new thread. My name is %s\n" % threading.currentThread().getName())
    sleepandprint()

print "Before starting a new thread,my name is", \
        threading.currentThread().getName()

# create new thread.
t =  threading.Thread(target=threadcode, name="ChildThread")

# this thread won't keep the program from terminating.
t.setDaemon(1)

# Start the new thread.
t.start()
sys.stdout.write("Hello from the new thread. My name is %s\n" % threading.currentThread().getName())
sleepandprint()

# Wait for the child thread to exit.
t.join()
