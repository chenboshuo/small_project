#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
from math import inf


class LingoOut():
    """对lingo结果文件的分析"""

    def __init__(self, filename):
        """打开文件,获取数据"""
        self.info = {}
        self.variable = {}
        self.decision = {}
        self.name = filename
        with open(filename) as file_object:
            for index, line in enumerate(file_object):
                # 读取 1-18 行为基本信息,
                if line != "\n" and 0 < index < 18 and index != 7:
                    self.info[line[2:line.find(':')]] = float(re.search("\d+(\.\d+)?", line).group(0))

                # 读取七行为模型类型
                elif index == 7:
                    self.info[line[2:line.find(':')]] = re.search("\w*$", line).group(0)

                # 读取19行之后的变量(这些数据以空行结束,空行之后终止循环)
                elif index > 19:
                    value = re.search('\d+.\d+', line)

                    # 若value匹配不成功,说明变量到了末尾行的回车
                    if not value:
                        break
                    value = float(value.group(0))
                    variable = re.search('\w*\(', line)

                    # 处理带索引的变量值
                    if variable:  # 匹配成功的话说明带索引
                        # 获得变量的值
                        variable = variable.group(0)[:-1]

                        # 匹配获得第一个索引 i
                        i = re.search('\( \d+', line)
                        i = int(i.group(0)[1:])

                        # 尝试匹配第二个索引
                        j = re.search(', \d+', line)

                        # 对有两个参数的情况进行处理
                        if j:
                            j = int(j.group(0)[1:])

                            # 判断变量是否有效,有效的话加入valid字典
                            if value == 1:
                                if not variable in self.decision.keys():
                                    self.decision[variable] = []
                                self.decision[variable].append((i, j))

                            # 将其他值加入字典
                            if not variable in self.variable.keys():
                                self.variable[variable] = {}
                            if not i in self.variable[variable].keys():
                                self.variable[variable][i] = {}
                            self.variable[variable][i][j] = value

                        else:  # 处理一个变量的情况
                            # 判断变量是否有效,有效的话加入valid字典
                            if value == 1:
                                if not variable in self.decision.keys():
                                    self.decision[variable] = []
                                self.decision[variable].append(i)

                            # 将其他值加入字典
                            if not variable in self.variable.keys():
                                self.variable[variable] = {}
                            self.variable[variable][i] = value
                    else:
                        variable = re.search('\w+', line).group(0)
                        self.variable[variable] = value

    def __str__(self):
        """调用print返回简单结果"""
        inofrmation = "Objective value:          %s\n" % self.info['Objective value']
        inofrmation += "Objective bound:          %s\n" % self.info['Objective bound']
        inofrmation += "Infeasibilities:          %s\n" % self.info['Infeasibilities']
        inofrmation += "Extended solver steps:    %s\n" % self.info['Extended solver steps']
        inofrmation += "Total solver iterations:  %s\n" % self.info['Total solver iterations']
        inofrmation += "Model Class:              %s\n" % self.info['Model Class']
        inofrmation += "Nonlinear variables:      %s\n" % self.info['Nonlinear variables']
        inofrmation += "Integer variables:        %s\n" % self.info['Integer variables']
        inofrmation += "Total constraints:        %s\n" % self.info['Total constraints']
        inofrmation += "Nonlinear constraints:    %s\n" % self.info['Nonlinear constraints']
        inofrmation += "Total nonzeros:           %s\n" % self.info['Total nonzeros']
        inofrmation += "Nonlinear nonzeros:       %s\n" % self.info['Nonlinear nonzeros']
        return inofrmation

    def __repr__(self):
        """获取对象的可解析字符串形式"""
        return f'LingoOut({self.name})'

    def __getitem__(self, key):
        """索引运算符(可以忽略大小写)
        输入字符,返回变量的值
        输入0,返回基本信息
        :param key: 变量的名字或0(显示基本信息)
        """
        if key == 0:
            print(self)
        else:
            key = key.upper()
            if key in self.variable:
                return self.variable[key]
            else:
                key = '"' + key + '"'
                return self.variable[key]

    def raw(self, line=inf):
        """显示原始的文件数据
        :param line: 打印的行数
        """
        with open(self.name) as file_object:
            for index, line_contents in enumerate(file_object):
                print(index + 1, line_contents, end=' ')
                if index + 1 >= line:
                    break
