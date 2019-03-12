#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Kelly Hwong on 2018年09月18日16:16:19

# Part A: House Hunting

import math

'''
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))
'''

# salary, saving, current_savings*r/12， annual_salary/12

# initinalize some examples for tests
# Test Case 1
'''
annual_salary = 120000
portion_saved = .05 # eg: 0.10
total_cost = 500000
semi_annual_raise = .03
# Number of months: 142
'''

# Test Case 2
'''
annual_salary = 80000
portion_saved = .1 # eg: 0.10
total_cost = 800000
semi_annual_raise = .03
# Number of months: 159
'''


# Test Case 3
annual_salary = 75000
portion_saved = .05 # eg: 0.10
total_cost = 1500000
semi_annual_raise = .05
# Number of months: 261

# constants
r = 0.04
portion_down_payment = 0.25


monthly_salary = annual_salary/12
down_payment = total_cost * portion_down_payment


current_savings = 0
mouth_count = 0

while current_savings < down_payment:
    # calc interests first
    additional_interest = current_savings*r/12
    current_savings += additional_interest

    # then added by saving
    current_savings += monthly_salary * portion_saved

    mouth_count += 1
    if mouth_count % 6 == 0:
        monthly_salary *= 1 + semi_annual_raise

print("Number of months: " + str(mouth_count))

# or current_savings *= 1 + r/12 after added by saving


