import sys

sys.path.append('../src/')
from LingoOut import LingoOut

filename = 'sample1.txt'

test = LingoOut(filename)

print("打印基本信息")
print(test)

print("查看变量字典")
print(test.variables)

# print("打印索引")
# print(test["x"])

print("打印决策变量字典")
print(test.decisions)
print(test[1])

print("打印原始数据前50行")
test.raw(50)
