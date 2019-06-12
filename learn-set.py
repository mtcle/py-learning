# set 学习,不允许重复元素
# set 使用大括号，没有key就是集合
set1 = {1, 2, 3, 4}
print(type(set1))

num1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]
# 去除重复元素，
num1 = list(set(num1))
print(num1)

# 常用方法
# add
# remove

set2 = {2, 3, 4, 5}
print(set2)
set2.add(99)
print(set2)

# 不可变集合
# 这样的set是不允许增删元素的
set3 = frozenset({1, 2, 3, 4, 5})

