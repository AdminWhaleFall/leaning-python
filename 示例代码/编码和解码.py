#encode()  decode()
# ascii
# gb2312  gbk
# unicode
# utf-8

#python3中字符串的两种类型：byte,str,str存储unicode类型，bytes存储byte类型

#字符串（unicode）转byte-----编码
a="我爱北京天安门"
b=a.encode("gbk")#转成字节码
#print(b)


#byte转字符串（unicode）----解码
c=b.decode("gbk")
print(c)

#编码方式和解码方式要一致


