'''
# 文件读写(IO操作) 持久化数据
# fh1--文件句柄 
fh1=open(r"E:\我的坚果云\Python 学习\test.txt","r") # r--read读取
# 读取文件 传入参数
data=fh1.read()
print(data)
fh1.close() #文件操作完毕后,一定要关闭文件IO资源
'''

'''
#读取文件
fh=open(r"E:\我的坚果云\Python 学习\test.txt","r")
# print(fh) #文件句柄
'''

# 一口气全部读取,赋值给data
'''
data=fh.read()
print(data)
fh.close()
'''

'''
# 按行读取
data=fh.readline()
print(data)
'''

'''
#按行读取所有 储存为列表
data=fh.readlines()
print(data)
'''

'''
# for循环遍历读取文件句柄 适合大文件读写
for i in fh:
	print(i)
fh.close() #文件操作完毕后,一定要关闭文件IO资源
'''

'''
#文件写入
fh=open("E:\我的坚果云\Python 学习\write.txt","w") # w--write 文件写入
#如果文件存在,则重新写入 如果文件不存,则新建一个文件并写入 文件夹要存在丫
data="我喜欢你,和我交往叭"
fh.write(data)
fh.close()
'''

'''
#文件追加写入
fh=open(r"E:\我的坚果云\Python 学习\write.txt","a")  #a--append 文件追加写入
data="那..好叭 我愿意 \n"
fh.write(data)
fh.close()
'''

# 所有文件分为 1.文本文件 2.二进制文件(音视频,图片,程序, .docx)
fh=open(r"E:\我的坚果云\Python 学习\1.jpg","rb") #rb--read binary读二进制文件
data=fh.read()
# print(data) #读取的是中间码
# 准备写入图片
fh2=open(r"E:\我的坚果云\Python 学习\wb.jpg","wb")
fh2.write(data)
fh.close()
fh2.close()





