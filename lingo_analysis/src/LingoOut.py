#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re


class LingoOut():
    """对lingo结果文件的分析"""

    def __init__(self, filename):
        """打开文件,获取数据"""
        self.info = {}
        self.variables = {}
        self.decisions = {}
        self.name = filename
        with open(filename) as file_object:
            for line in file_object:
                # 寻找标识":"
                info_sign = line.find(':')
                value = re.search(r"[\-]?[\d]+(\.[\d]*)([Ee][+-]?[\d]+)?", line)  # 匹配科学记数法
                # info 匹配成功,则为信息行
                if info_sign > 0:
                    value = re.search(r"\d+(\.\d+)?", line)
                    if value:
                        self.info[line[2:info_sign]] = float(value.group(0))
                    else:
                        self.info[line[2:line.find(':')]] = re.search(r"\w*$", line).group(0)

                elif line.find('Row') > 0:  # 忽略那些每行的误差(就读取到变量行之前)
                    break
                elif value:
                    value = float(value.group(0))
                    variable = re.search(r'\w*\(', line)

                    # 处理带索引的变量值
                    if variable:  # 匹配成功的话说明带索引
                        # 获得变量的值
                        variable = variable.group(0)[:-1].lower()

                        # 匹配获得第一个索引 i
                        i = re.search(r'\( \d+', line)
                        i = int(i.group(0)[1:])

                        # 尝试匹配第二个索引
                        j = re.search(r', \d+', line)

                        # 对有两个参数的情况进行处理
                        if j:
                            j = int(j.group(0)[1:])

                            # 判断变量是否有效,有效的话加入valid字典
                            if value == 1:
                                if variable not in self.decisions.keys():
                                    self.decisions[variable] = []
                                self.decisions[variable].append((i, j))

                            # 将其他值加入字典
                            if variable not in self.variables.keys():
                                self.variables[variable] = {}
                            if not i in self.variables[variable].keys():
                                self.variables[variable][i] = {}
                            self.variables[variable][i][j] = value

                        else:  # 处理一个变量的情况
                            # 判断变量是否有效,有效的话加入valid字典
                            if value == 1:
                                if variable not in self.decisions.keys():
                                    self.decisions[variable] = []
                                self.decisions[variable].append(i)

                            # 将其他值加入字典
                            if variable not in self.variables.keys():
                                self.variables[variable] = {}
                            self.variables[variable][i] = value
                    else:
                        variable = re.search(r'\w+', line).group(0).lower()
                        self.variables[variable] = value

    def __str__(self):
        """调用print返回简单结果"""
        s = ""
        for keys, value in self.info.items():
            s += "{:30}{:>20}\n".format(keys, value)  # 30个字符, 20个字符右对齐
        return s

    def __repr__(self):
        """获取对象的可解析字符串形式"""
        return f'LingoOut({self.name})'

    def __getitem__(self, key):
        """索引运算符(可以忽略大小写)
        输入字符,返回变量的值
        输入0,返回基本信息
        :param key: 变量的名字或0(显示基本信息),1(返回决策变量的字典)
        """
        if key == 0:
            print(self)
        elif key == 1:
            return self.decisions
        else:
            if key in self.variables:
                return self.variables[key]
            else:
                key = '"' + key + '"'
                return self.variables[key]

    def raw(self, limit=-1):
        """显示原始的文件数据
        :param limit: 打印的行数
        """
        if limit > 0:
            with open(self.name) as file_object:
                for index, line_contents in enumerate(file_object.readlines()[0:limit]):
                    print(index + 1, line_contents, end=' ')
        else:
            with open(self.name) as file_object:
                for index, line_contents in enumerate(file_object):
                    print(index + 1, line_contents, end=' ')
