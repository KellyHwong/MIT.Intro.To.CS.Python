#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: kelly hwong
# Date: 2018.10.25

class Baby(object):

    def __init__(self, birthday, sex, name, weight):
        super(Baby, self).__init__()
        self.birthday = birthday # 时间字符串
        self.sex = sex # 性别，Boy or Girl
        self.name = name # 名字，字符串
        self.weight = weight # 公斤
        print("Hello! " + self.name + " Daddy/Mommy welcomes you to the World!")

myBaby = Baby("2018年10月25日14:10:52", "Boy", "琪琪", "3.5")

