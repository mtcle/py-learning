import random

randSum = random.randint(0, 10)
print(randSum)
index = 0
# while 循环
while index < randSum:
    print(index)
    index += 1

# array 数组遍历
numbers = [1, 3, 5, 7, 9]
numbers2 = list(range(1, 5, 2))
for i in numbers2:
    print("数组遍历：" + str(i))
# list 增加元素
numbers2.append(88)
print("append后：" + str(numbers2))

# 元组 类似列表,不能改变里面的数据
tuple1 = 1, 2, 3
tuple2 = (1, 2, 3)
print(type(tuple1))


def method():
    """我是文档注释，可以通过doc查看"""
    # 我是注释
    print("我是调用方法")


method()
print(method.__doc__)


def method2(key1, key2):
    """根据形参进行输入参数"""
    print(key1)
    print(key2)


method2(key2="我是第二个参数", key1="我是第一个参数")


def method3(*parmas):
    """我是不定参数函数"""
    print(parmas)


method3(1, 2, 3, 4, "111")


globalNum=10


def method4():
    # globalNum=5 #这个globalNum并不是外面那个
    # 用global关键字修饰变量是全局的那个，进行修改
    global globalNum
    globalNum = 5
    print(globalNum)


method4()
print(globalNum)
