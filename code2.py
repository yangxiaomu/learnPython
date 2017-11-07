#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
# 奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
# 可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


# stupid
def getBonus1(profit):
    bonus = 0
    if profit - 100000 < 0:
        bonus = profit*0.1
    elif profit - 200000 < 0:
        bonus = 100000*0.1 + (profit - 100000)*0.075
    elif profit - 400000 < 0:
        bonus = 100000*0.1 + (profit - 100000)*0.075 + (profit - 200000)*0.05
    elif profit - 600000 < 0:
        bonus = 100000 * 0.1 + (profit - 100000) * 0.075 + (profit - 200000) * 0.05 + (profit - 400000)*0.03
    elif profit - 1000000 < 0:
        bonus = 100000 * 0.1 + (profit - 100000) * 0.075 + (profit - 200000) * 0.05 + (profit - 400000)*0.03 + (profit - 600000)*0.015
    else:
        bonus = 100000 * 0.1 + (profit - 100000) * 0.075 + (profit - 200000) * 0.05 + (profit - 400000)*0.03 + (profit - 600000)*0.015 + (profit-1000000)*0.01

    return bonus


# dic 没顺序啊。。。。
# 百度：
# Python的Hash实现是基于Open Addressing的。当你搜索所有的key的时候
# 实际上就是遍历整个表，寻找那些value不为null的entry，然
# 后把它们的key放到一个list里面，这个 过程自然是不保证顺序的。
def getBonus2(profit):
    bonus = 0
    level = {1000000 :0.01, 600000 : 0.015, 400000 : 0.03, 200000 : 0.05, 100000 : 0.075, 0 : 0.1}

    for i in level.keys():
        if profit - level[i] > 0:
            profit = profit - i
            bonus = bonus + profit*level.get(i)
            profit = i

    return bonus

def getBonus3(profit):
    bonus = 0
    level = [10,6,4,2,1,0]
    rate = [0.01,0.015,0.03,0.05,0.075,0.1]
    for i in xrange(0,6):
        if profit - level[i]*100000 > 0:
            profit = profit - level[i]*100000;
            bonus = bonus + profit*rate[i]
            profit = level[i]

    return bonus

profit = int(raw_input("Please input the profit:"))
print "func1 Bonus:", getBonus1(profit)
print "func2 Bonus:", getBonus2(profit)
print "func3 Bonus:", getBonus3(profit)