import re

'''
#compile函数:将正则表达式转换成内部格式,提高执行效率
strr="Python666Java"
# 旧方法
# pat=r"\d+"
# print(re.search(pat,strr))
# compile提高运行效率
pat=re.compile(r"python",re.I) # re.I模式修正符,忽略大小写
print(pat.search(strr))
'''

# match函数:匹配开头位置
# search函数:匹配任意位置
# 两个函数都是一次匹配,匹配到一次就不再向后继续匹配了
'''
strr="JAvApythonjavahtmljs"
pat=re.compile(r"(j)ava",re.I)
# .group() 输出匹配到的内容 若分组则可以传组数
print(pat.search(strr).group())
'''

# findall() 查找所有匹配的内容,装到列表中
# finditer()  查找所有匹配的内容,装到“迭代器”中

'''
strr="hello-----hellllo---hello--------\
-----ohellohe--------hell-----ohello-----\
----hello---hello-----------hello-----"

pat=re.compile(r"hello")
# print(pat.findall(strr)) #是个列表 全局寻找
data=pat.finditer(strr) #不能直接显示,要用for循环遍历

list1=[]
for i in data:
	# print(i.group())
	list1.append(i.group())

#要哪个就可以取哪个 效率可能会高一些
print(list1)
'''

# split() 按照能够匹配的子串将字符串分割后返回列表
# sub() sub方法 用于替换

strr = "花子君,,,,,,,,,八寻宁宁,,,,,,,魏无羡,,,,,蓝忘机"

pat = re.compile(r",+")
print(pat.findall(strr))
print(pat.split(strr))

strr2 = "hello 123,hello 456!"
# 匹配多个数字
pat2 = re.compile(r"\d+")
# 替换后,替换的字符
result = pat2.sub("666", strr2)
print(result)
