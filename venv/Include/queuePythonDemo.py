#!/usr/bin/env python
# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: queuePythonDemo.py

@time: 2018/4/4 11:19

@desc:

'''
import threading
import time
import Queue
status = 0


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        print "111"
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name+"\n"
        print "112"
        process_data(self.name, self.counter)

        print "Exiting " + self.name


def process_data(threadName, counter):
    print "113"
    while not status:
        queueLock.acquire()
        if not workQueue.empty():
            data = counter.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)


print ("114")
threadList= ["thread-1","thread-2","thread-3"]
nameList= ["one","two","three","four","five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threadId= 1
threads = []

for tname in threadList:
    print "115"
    thread = myThread(threadId,tname,workQueue)
    thread.start()
    threads.append(thread)
    threadId +=1
print "116"
queueLock.acquire()
for work in nameList:
    workQueue.put(work)
queueLock.release()

while not workQueue.empty():
    pass

status =1
for t in threads:
    t.join()

print "exit Main Thread"
