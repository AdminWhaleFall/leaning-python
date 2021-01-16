import re

#原子：正则表达式中实现匹配的基本单位
#元字符：正则表达式中具有特殊含义的字符

#以普通字符作为原子（匹配一个普通字符）
a="湖南湖北广东广西"

pat="湖北"

result=re.search(pat,a)


print(result)

