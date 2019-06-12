# coding=gbk
list1 = [1, 2, 3]
try:
    print(list1[4])
except Exception as reason:
    print("怎么搞得，怎么异常了！！")
    print('错误原因：', str(reason))
finally:
    print("程序执行完成，走到finally")

