# coding=gbk
# �����Ӷ��󱣴浽file�л��߷�����,�����ݵĳ־û�
import pickle

myList = [111, 333, 444, 4.33, "��������������", [3333, 334]]

pickle_file = open("myListStoreFile.pkl", "wb")  # ������д��ģʽ
pickle.dump(myList, pickle_file)
pickle_file.close()

pickle_file = open("myListStoreFile.pkl", "rb")  # ������д��ģʽ
readList = pickle.load(pickle_file)
pickle_file.close()
print("��ȡ�����ݣ�", readList)
