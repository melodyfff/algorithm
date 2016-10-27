#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：暂停一秒输出。
import time
print('time.time():',time.time())
print('time.localtime(time.time()):',time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))