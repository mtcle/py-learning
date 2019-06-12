# 操作文件
# 读文件
file = open("./doc.txt", "r")
txt = ""
for eachLine in file:
    print(eachLine)
file.close()

# 写文件,以可读写模式打开文本
file = open("./doc.txt", "a+")
file.write("我是追加的内容\n")
file.seek(0, 0)  # 将文件指针回退到初始位置
for eachLine in file:
    print(eachLine)
file.close()
