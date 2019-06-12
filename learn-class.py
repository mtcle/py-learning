# coding=gbk
# python 类 对象使用,类必须大写打头


class Person:
    # 属性
    legs = 2  # 两条腿

    __age = 10  # 双下划线打头，私有变量

    # 重写默认构造方法
    def __init__(self, legs):
        self.legs = legs
        self.__age = 20

    # 方法
    def eat(self, val):
        print("eat something: ", val)


man = Person(4)
man.eat("apple")
print(man.legs)


# print(man.__age) 私有成员无法获取


# 继承,Man 继承自Person，python支持多继承，在括号里面写多个即可，逗号分开
class Man(Person):
    beardColor = "white"

    def __init__(self, color):
        super().__init__(2)
        self.beardColor = color


zhangFei = Man("black")
print("张飞有 %d 条腿！胡子是 %s 色的！" % (zhangFei.legs, zhangFei.beardColor))

print(isinstance(zhangFei, Person))
print(issubclass(Man, Person))
print(issubclass(Man, Person))
print(getattr(zhangFei, "legs", "没有该字段"))
print(getattr(zhangFei, "height", "没有该字段"))


