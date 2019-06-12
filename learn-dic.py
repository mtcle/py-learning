# 字典数据类型学习，类似java的map
# 大括号是字典，中括号是数组，小括号加逗号 是元组
dic1 = {"李宁": "一切皆有可能！", "耐克": "Just do it!"}
print(dic1)
dic1["没有的key"] = "我是新赋值的字段"
print(dic1)
print(dic1["耐克"])

print("字典dic1的长度：",len(dic1))
# 遍历dic
for k in dic1.keys():
    print(k, "->", dic1[k])
    print(k, "->", dic1.get(k, "如果没有key时的默认值！"))

# dic的方法，
# clear 清空字典
# 字典里面的popitem 不是栈，不是pop最上面的，是随机，字典无序
