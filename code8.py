#!/usr/bin/python
#coding=utf-8

# 题目：输出 9*9 乘法口诀表。

for i in xrange(1,10):
    a = []
    for j in xrange(1,10):
        if j>i:
            break
        a.append(str(i)+"*"+str(j)+"="+str(i*j))
    print a


for i in xrange(1,10):
    print
    for j in xrange(1,10):
        print "{}*{}={}".format(j, i, j * i),
        if j==i:
            break