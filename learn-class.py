# coding=gbk
# python �� ����ʹ��,������д��ͷ


class Person:
    # ����
    legs = 2  # ������

    __age = 10  # ˫�»��ߴ�ͷ��˽�б���

    # ��дĬ�Ϲ��췽��
    def __init__(self, legs):
        self.legs = legs
        self.__age = 20

    # ����
    def eat(self, val):
        print("eat something: ", val)


man = Person(4)
man.eat("apple")
print(man.legs)


# print(man.__age) ˽�г�Ա�޷���ȡ


# �̳�,Man �̳���Person��python֧�ֶ�̳У�����������д������ɣ����ŷֿ�
class Man(Person):
    beardColor = "white"

    def __init__(self, color):
        super().__init__(2)
        self.beardColor = color


zhangFei = Man("black")
print("�ŷ��� %d ���ȣ������� %s ɫ�ģ�" % (zhangFei.legs, zhangFei.beardColor))

print(isinstance(zhangFei, Person))
print(issubclass(Man, Person))
print(issubclass(Man, Person))
print(getattr(zhangFei, "legs", "û�и��ֶ�"))
print(getattr(zhangFei, "height", "û�и��ֶ�"))


