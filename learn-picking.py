# coding=gbk
# 将复杂对象保存到file中或者反过来,做数据的持久化
import pickle

myList = [111, 333, 444, 4.33, "哈哈哈，真随意", [3333, 334]]

pickle_file = open("myListStoreFile.pkl", "wb")  # 二进制写的模式
pickle.dump(myList, pickle_file)
pickle_file.close()

pickle_file = open("myListStoreFile.pkl", "rb")  # 二进制写的模式
readList = pickle.load(pickle_file)
pickle_file.close()
print("读取的数据：", readList)
