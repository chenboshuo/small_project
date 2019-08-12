#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   chenboshuo.hi@163.com
@Software: PyCharm 
@Time    : 2019/8/11 20:17
Copyright (c) 2019 ChenBoshuo. All rights reserved.
"""

import sys

sys.path.append('../src/')
from LingoOut import LingoOut


def a_test(filename):
    """
    一个测试
    :param filename:
    :return:
    """
    test = LingoOut(filename)

    print("打印基本信息")
    print(test)

    print("查看变量字典")
    print(test.variable)

    # print("打印索引")
    # print(test["x"])

    print("打印决策变量字典")
    print(test.decision)
    print(test[1])

    print("打印原始数据前50行")
    test.raw(50)


a_test("test1.txt")
a_test("test2.txt")
a_test("test3.txt")
