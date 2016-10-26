#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），
# 又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0    (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)
from Tools.scripts.treesync import raw_input

# def fib():
n = int(raw_input('define n(n=>1) = '))
if (n < 1):
    print('error number!')
a,b= 0,1
for i in range(n):
    print(a, end="\t")
    a, b = b, a + b

# def fib1(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
#
# # 输出了第10个斐波那契数列
# print(fib1(1))
# print(fib())

