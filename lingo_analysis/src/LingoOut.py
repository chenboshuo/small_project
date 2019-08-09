import re

class LingoOut():
    """对lingo结果文件的分析"""
    def __init__(self,filename):
        self.dict = {}
        self.variable = {}
        self.valid = []
        with open(filename) as file_object:
            for line in file_object:
                # 按照连续空格分隔关键字
                line_list = line.split('  ')
                
                # 快速去掉空字符串
                line_list = list(filter(None, line_list)) 
                
                # 去掉空行(单个'\n')
                if len(line_list) >= 2:
                    try:
                        self.dict[line_list[0]] = float(line_list[1][:-1]) #[:-1 去掉每行末尾的\n]
                    except:
                        self.dict[line_list[0]] = line_list[1][:-1]
                        
        # 对变量进行处理
        for key,value in self.dict.items(): 
            # 匹配字符串和数字
            var = re.search('\w*\(', key)
            index = re.findall('\d+', key)
            
            # 寻找值为1的变量
            if var and type(value) == float  and value == 1:
                self.valid.append(key) 
            
            if var and len(index) == 1:
                index_1 = int(index[0])
                var = var.group(0)[:-1]                
                try:
                    self.variable[var][index_1] = value
                except KeyError:
                    self.variable[var] = {}
            if var and len(index) == 2:
                var = var.group(0)[:-1]
                index_1 = int(index[0])
                index_2 = int(index[1])
                try:
                    self.variable[var]
                except KeyError:  
                    self.variable[var] = {}
                try:
                    self.variable[var][index_1]
                except KeyError:
                    self.variable[var][index_1] = {}
                self.variable[var][index_1][index_2] = value
    def __str__(self):
        """调用print返回简单结果"""
        str =  "Objective value:          %s\n" % self.dict['Objective value:']
        str += "Objective bound:          %s\n" % self.dict['Objective bound:']
        str += "Infeasibilities:          %s\n" % self.dict['Infeasibilities:']
        str += "Extended solver steps:    %s\n" % self.dict['Extended solver steps:']
        str += "Total solver iterations:  %s\n" % self.dict['Total solver iterations:']
        str += "Model Class:              %s\n" % self.dict['Model Class:']
        str += "Nonlinear variables:      %s\n" % self.dict['Nonlinear variables:']
        str += "Integer variables:        %s\n" % self.dict['Integer variables:']
        str += "Total constraints:        %s\n" % self.dict['Total constraints:']
        str += "Nonlinear constraints:    %s\n" % self.dict['Nonlinear constraints:']
        str += "Total nonzeros:           %s\n" % self.dict['Total nonzeros:']
        str += "Nonlinear nonzeros:       %s\n" % self.dict['Nonlinear nonzeros:']
        return str



