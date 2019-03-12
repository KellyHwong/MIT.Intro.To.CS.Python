#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Kelly Hwong on 2018年09月18日16:16:19

# Part A: House Hunting

import math

# Test Case 1
# annual_salary = 150000
# # out
# portion_saved = 0.4411
# Steps in bisection search: 12
# 我的答案
# Best savings rate: 0.4256
# Steps in bisection search: 8

# Test Case 2
# annual_salary = 300000
# # out
# portion_saved = 0.2206
# Steps in bisection search: 9
# 我的答案
# Best savings rate: 0.2128
# Steps in bisection search: 13


# Test Case 3
# annual_salary = 10000
# # out
# portion_saved = impossible
# Steps in bisection search: impossible


# Note: There are multiple right ways to implement 
# bisection search/number of steps so your results
# may not perfectly match those of the test case.


# annual_salary = int(input("Enter the starting salary: "))
# constants

# annual_salary = 10000
# annual_salary = 300000
annual_salary = 150000

CONST_IMPOSSIBLE = """It is not possible to pay the down payment in three years."""
r = 0.04
total_cost = 1000000 # $1M
semi_annual_raise = .07
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment





# 刚好三年 36个月存下来
# 能够存下来，求最少的存款率
# 有的情况不能存下来，比如 Test Case 3 的情况
# 那么要从极端开始，100% 来下降
# your savings to be within $100 of the required down payment.

# calculate the best savings rate, as a function of your starting salary



# 
# bisection search

# 定义函数 calcFinalSaving
def calcFinalSaving(monthly_saved):
    # calc savings after 36 months
    # can be wrapped as a function
    current_savings = 0
    mouth_count = 0

    while mouth_count <= 36:
        # calc interests first
        additional_interest = current_savings*r/12
        current_savings += additional_interest

        # then added by saving
        current_savings += monthly_saved

        mouth_count += 1 # previous month ends, new month begins
        if mouth_count % 6 == 0:
            monthly_saved *= 1 + semi_annual_raise

    return current_savings

def main():
    # print(calcFinalSaving(annual_salary/12.0*6.39/100))

    # init 
    bisection_steps = 0
    # integer between 0 and 10000
    # 0<= ? <= 10000
    start = 0
    index = 10000 # begins from maximum
    end = 10000
    portion_saved = index/10000.0 # decimal percentage
    monthly_salary = annual_salary/12

    # 按照维基百科的方法写，不portion_saved过，开头要写一个边缘检测
    current_savings = calcFinalSaving(monthly_salary * portion_saved)

    # print("current_savings:", current_savings)

    if current_savings < down_payment - 100:
        print(CONST_IMPOSSIBLE)
        return
    else:
        while start <= end:
            mid = start + (end - start) / 2 # 直接平均可能會溢位，所以用此算法 from 维基
            portion_saved = mid/10000.0 # decimal percentage
            bisection_steps += 1
            # two conditions
            # less than down_payment
            current_savings = calcFinalSaving(monthly_salary * portion_saved)
            if current_savings < down_payment - 100:
                start = mid + 1 # increase the saving rate
            # more than down_payment
            elif current_savings > down_payment + 100:
                end = mid - 1
            else:
                # got the best savings rate
                print("Best savings rate: " + str(mid/10000.0))
                print("Steps in bisection search: " + str(bisection_steps))
                return mid

if __name__ == '__main__':
    main()
