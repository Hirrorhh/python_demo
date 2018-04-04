#!/usr/bin/env python
# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: threadLockPythonDemo.py

@time: 2018/4/2 13:52

@desc:

'''
import threading
import time
status = 0


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        print "Exiting " + self.name
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        if status:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


threadLock = threading.Lock()
threads = []
#创建2个新的线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
#线程启动
thread1.start()
thread2.start()
#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print "Exiting Main Thread"