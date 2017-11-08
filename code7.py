#!/usr/bin/python
#coding=utf-8

# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。


a = [1,2,3,4,5,6,7,8]
b = []

c = a[:]

len = len(a)
b.extend(a[0:len])
print b
print c