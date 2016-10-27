#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 异或相同为假不同为真
# 题目：a和b不通过第三个变量来交换值
# 1^1=0 0^0=0
# 1^0=1 0^1=1
#
from Tools.scripts.treesync import raw_input

a=2
b=5
a=a^b #7
b=a^b #2
a=a^b #5
print(a,b)

# n=int(raw_input("颜色种数"))
#
# l=[]
# for i in range(3):
#     x=int(input("input:"))
#     if x != '\n':
#      l.append(x)
# else:
#     print(l)

print(bin(10).replace('0b',''))
