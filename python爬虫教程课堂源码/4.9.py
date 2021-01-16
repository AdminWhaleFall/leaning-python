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


#原子表
#定义一组平等的原子
# b="18689276390"
# pat2="1[3578]\d\d\d\d\d\d\d\d\d"
# print(re.search(pat2,b))

# c="nsiwsoiwpythonjsoksosj"
# pat3=r"py[abcdt]hon"

# print(re.search(pat2,b))





#元字符--正则表达式中具有特殊含义的字符
# . 匹配任意字符 \n除外
# ^ 匹配字符串开始位置  ^136
# $ 匹配字符串中结束的位置 6666$
# * 重复0次1次多次前面的原子 \d*
# ? 重复一次或者0次前面的原子 \d?
# + 重复一次或多次前面的原子  \d+

# d="135738484941519874888813774748687"
# pat1="..."
# pat2="^135\d\d\d\d\d\d\d\d"
# pat3=".*8687$"
# pat4="8*"
# pat5="8+"
# print(re.search(pat5,d))





#匹配固定次数
#{n}前面的原子出现了n次
#{n,}至少出现n次
#{n,m}出现次数介于n-m之间

# a="234ded65de45667888991jisw"
# pat1=r"\d{8,10}"

# print(re.search(pat1,a))





# #多个表达式 | 
# a="13699998888"
# b="027-1234567"

# pat1=r"1[3578]\d{9}|\d{3}-\d{7}"

# print(re.search(pat1,a))



