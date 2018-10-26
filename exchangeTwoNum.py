#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: exchangeTwoNum.py
# Created by Kelly Hwong on 2018年10月04日01:01:51

# 参考：https://blog.csdn.net/lpt19832003/article/details/5334688
# 他是这么写的：

'''
    a = a ^ b;
    b = b ^ a;
    a = a ^ b;
'''

a = 3
b = 7

# 建议这么写，好记，a b a，然后三个a ^ b
a = a ^ b # a2 = a1 ^ b1
b = a ^ b # b2 = a2 ^ b1 = a1 ^ b1 ^ b1 = a1
a = a ^ b # a3 = a2 ^ b2 = a2 ^ a1 = a1 ^ b1 ^ a1 = b1

print("a=" + str(a))
print("b=" + str(b))

'''
a=7
b=3
[Finished in 0.2s]
'''