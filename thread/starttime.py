#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import _thread


# 为线程定义函数


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 5))
    _thread.start_new_thread(print_time, ("Thread-2", 10))
except:
    print("Error:无法启动")

while 1:
    pass
