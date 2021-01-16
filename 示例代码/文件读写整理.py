IO操作 （对磁盘进行持久化文件的读取和写入）

#1.r读取文本文件,fh是文件句柄
#如果有编码错误，参数加上encoding="utf-8或者gbk"*****
f1=open(r"C:\aaadir\001.txt","r")
data=f1.read()#读取全部文件
data=f1.readline()#一行一行读取，每执行一次读取一行
data=f1.readlines()#按行读取，每一行作为列表中的一个元素
print(data)
f1.close()#关闭文件资源


#2.文件的指针，连续读两次演示*****
f1=open(r"C:\aaadir\001.txt","r")
data1=f1.read()
print(f1.tell())#获取文件指针所在位置
f1.seek(0)#手动设置文件指针所在位置,定位到开头
data2=f1.read()
print(data2)
f1.close()


#3.读取大文件*****
f1=open(r"C:\aaadir\001.txt","r")
for line in f1:
	print(line)
	f1.close()








#4.w写文件,写的时候不能读，读的时候不能写*****
f1=open(r"C:\aaadir\003.txt","w")
#文件存在就清空再写入，不存在就先创建
f1.write("hello")
f1.close()









#5.a追加模式写文件*****
f1=open(r"C:\aaadir\003.txt","a")
f1.write("你好")
f1.close()



#6.r+读写模式,既能读又能以追加的模式写
#如果写的位置上已经有文本，会直接替换
f1=open(r"C:\aaadir\003.txt","r+")
print(f1.read())
f1.write("hello")
f1.close()


#7.w+写读模式
#文件存在就清空再写入，不存在就先创建
f1=open(r"C:\aaadir\003.txt","w+")
f1.write("hello")
f1.seek(0) #写入之后，文件定位到了末尾，读的时候需要重新定位到开头
print(f1.read())
f1.close()


#8.a+追加读写模式
#和r+不同点：a+模式在读的时候自动定位到开头，
#写的时候自动定位到末尾
#a+模式中如果文件不存在就会创建，而r+会报错
f1=open(r"C:\aaadir\003.txt","a+")
f1.write("hello")
f1.seek(0)
print(f1.read())
f1.close()



#所有的文件分为两大类：1.文本文件   2.二进制文件

#9.读写二进制文件，加上b即可，基本逻辑与文本文件一样 *****读二级制文件
#读写二进制文件不要设置编码格式
#这里以复制一个图片为例：
f1=open(r"C:\aaadir\001.jpg","rb")
f2=open(r"C:\aaadir\001.jpg","wb")
f2.write(f1.read())#普通
for i in f1:#大文件写入
	f2.write(i)
f1.close()






#10.异常处理
try:
	f1=open(r"C:\aaadir\001.jpg","rb")
	f2=open(r"C:\bbbdir\001.jpg","wb")
	f2.write(f1.read())
except Exception as e:
	raise e
finally:
	f1.close()


#还有一种方式,会自动处理异常，而且会帮我们关闭文件句柄：*****
with open(r"C:\aaadir\001.jpg","rb") as f1,open(r"C:\bbbdir\001.jpg","wb") as f2:
	f2.write(f1.read())




#11.附加：文件重命名和删除
#import os
# os.rename("F:/001.txt","F:/111.txt")
# os.remove("F:/003.txt")
# os.mkdir("文件夹路径")





