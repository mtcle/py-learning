# coding=gbk
list1 = [1, 2, 3]
try:
    print(list1[4])
except Exception as reason:
    print("��ô��ã���ô�쳣�ˣ���")
    print('����ԭ��', str(reason))
finally:
    print("����ִ����ɣ��ߵ�finally")

