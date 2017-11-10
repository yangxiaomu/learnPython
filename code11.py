#!/usr/bin/python
#coding=utf-8

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

# 2,2,4,6,10,16

def count(day):
    if day == 1 or day == 2:
        return 2
    else:
        return count(day-1)+count(day-2)


print count(10)
