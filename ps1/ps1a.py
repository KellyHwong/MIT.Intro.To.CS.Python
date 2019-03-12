#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Kelly Hwong on 2018年09月18日16:16:19

# Part A: House Hunting

import math

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))


# salary, saving, current_savings*r/12， annual_salary/12

# initinalize some examples for tests
# annual_salary = 120000
# portion_saved = .10 # eg: 0.10
# total_cost = 1000000

# annual_salary = 80000
# portion_saved = .15 # eg: 0.10
# total_cost = 500000

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

print("Number of months: " + str(mouth_count))

# or current_savings *= 1 + r/12 after added by saving


