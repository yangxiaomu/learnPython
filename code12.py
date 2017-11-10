#!/usr/bin/python
# coding=utf-8

# 题目：判断101-200之间有多少个素数，并输出所有素数
#

import math

for i in range(101,200):
    flag = 1
    for j in range(2,int (math.sqrt(i+1))):
        if i%j != 0:
            pass
        else:
            flag = 0
            break
    if flag == 1:
        print i