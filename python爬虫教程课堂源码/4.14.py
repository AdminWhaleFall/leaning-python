import re

#findall()   查找所有匹配的内容，装到列表中
#finditer()  查找所有匹配的内容，装到迭代器中

strr="hello--------hello-----------\
---------hello-----------------\
---------hello--hello----------------\
----------hello---------hello----hello----------"

pat=re.compile(r"hello")

#print(pat.findall(strr))
data=pat.finditer(strr)

list1=[]

for i in data:
	list1.append(i.group())

print(list1)