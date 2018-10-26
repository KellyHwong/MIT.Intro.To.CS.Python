#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: kelly hwong
# Date: 2018.4.25

# 用迭代的方法算乘法
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# MULTIPLICATION – RECURSIVE SOLUTION
def mult(a, b):
    if b == 1:
        return a # base case
    else:
        return a + mult(a, b - 1) # recursion step

# factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
# 加b次a
    a = 3
    b = 5
    # result = mult(a, b)
    # print(result)
    print(factorial(4))

if __name__ == '__main__':
    main()