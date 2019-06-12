# os模块
import os

print("当前系统：", os.name)
print("当前工作目录：", os.getcwd())
print("目录文件：", os.listdir())

print("新建文件目录：", os.makedirs("./newfiles/b"))
# 删除目录
os.removedirs("./newfiles/b")
# 打开系统程序
# os.system("cmd")

# 文件路径操作
print(os.path.basename('./doc.txt'))
print(os.path.dirname('./doc.txt'))
print(os.path.getsize('./doc.txt'), "字节")

# 时间模块
import time
print(time.localtime())