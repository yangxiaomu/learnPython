#!/usr/bin/python
#coding=utf-8

# 输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(raw_input("Please input x:"))
y = int(raw_input("Please input y:"))
z = int(raw_input("Please input z:"))

list = []
list.append(x)
list.append(y)
list.append(z)

#
# for i in range(0,3):
#   for j in range(i,3) :
#      if (list[i] >= list[j] ):
#          tmp =list[i]
#          list[i]=list[j]
#          list[j]=tmp
#
list.sort();

print list