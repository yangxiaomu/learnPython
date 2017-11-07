#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

result = []
for x in xrange(1, 5):
    for y in xrange(1, 5):
        for z in xrange(1, 5):
            if x != y and x != z and y != z:
                result.append([x, y, z])

print "length:", len(result)
print result
