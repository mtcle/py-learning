# lambda表达式
def method1(x):
    return x * 2


method2 = lambda x: x * 2

print(method2(2))

total = 0


# 汉诺塔 递归调用
def hannuota(n, x, y, z):
    global total
    if n == 1:
        print("从", x, "-->", z)
        total += 1
    else:
        # 将前n-1个子从x移动到y上
        hannuota(n - 1, x, z, y)
        # 将最底下的最后一个盘子从x移动到z上面
        # print("从", x, "-->", z)
        # 然后将y上面的n-1个盘子移动到x上面
        hannuota(n - 1, y, x, z)
        total += 1
    return total


n = int(input("请输入汉诺塔层数："))
number = hannuota(n, 'X', 'Y', 'Z')
print(number)
