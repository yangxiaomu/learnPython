#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

input_date = raw_input("Please input the date(format:YYYYMMDD):")

year = int(input_date[0:4])
month = int(input_date[4:6])
day = int(input_date[6:8])

if year % 4 == 0:
    feb_days = 29
else:
    feb_days = 28

month_days = [31,feb_days,31,30,31,30,31,31,30,31,30,31]

days = day
while month >1 :
    days = days + month_days[month-2]
    month -= 1

print "The year's :",days,"th days"