import sys

print(sys.path)
# sys.path.insert(0, "/path/to/my/modules")
# print(sys.path)

import math
print(dir(math)) 

def total_sum(data):
    return sum(data)

print(total_sum([1,2,3]))        # 列表
print(total_sum((4,5,6)))        # 元组
print(total_sum({7,8,9}))        # 集合