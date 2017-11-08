#!/usr/bin/python
#coding=utf-8

# 题目：斐波那契数列。

# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)


def fibo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)


a = int(raw_input("Please input the N："))

print fibo(a)