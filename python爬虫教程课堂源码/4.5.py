import re

#原子：正则表达式中实现匹配的基本单位
#元字符：正则表达式中具有特殊含义的字符

#以普通字符作为原子（匹配一个普通字符）
# a="湖南湖北广东广西"
# pat="湖北"
# result=re.search(pat,a)
# print(result)


#匹配通用字符
#\w 任意字母/数字/下划线 
#\W 和小写w相反 
#\d 十进制数字
#\D 除了十进制数以外的值
#\s 空白字符 
#\S 非空白字符 

# b="136892763900"
# pat2="1\d\d\d\d\d\d\d\d\d\d"
# print(re.search(pat2,b))

# c="@@@@@@@@@@##@!_tdyuhdihdiw"
# pat3=r"\W\w\w"
# print(re.search(pat3,c))


#匹配数字、英文、中文
# 数字 [0-9]
# 英文 [a-z][A-Z]
# 中文 [\u4e00-\u9fa5]

# d="!@#$@#@##$张三%$^%$%#@$boy#@%##$%$$@#@#23@#@#@#@##$%$%$"

# pat1=r"[\u4e00-\u9fa5][\u4e00-\u9fa5]"
# pat2=r"[a-z][a-z][a-z]"
# pat3=r"[0-9][0-9]"

# result1=re.search(pat1,d)
# result2=re.search(pat2,d)
# result3=re.search(pat3,d)

# print(result1,result2,result3)


