import re

#compile函数---将正则表达式转换成内部格式，提高执行效率

strr="PYTHON666Java"

pat=re.compile(r"Python",re.I) #模式修正符：忽略大小写


print(pat.search(strr))
