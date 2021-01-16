#正则表达式
#数据筛选(针对字符串)的表达式 (匹配)

import re #正则表达式模块
'''
strr="花子君八寻宁宁人鱼公主"

pat="八寻"
# 在strr里面找符合pat的内容
rst=re.search(pat,strr)
print(rst)
'''

#原子:正则表达式中实现匹配的基本单位
# 元字符:正则表达式中含有特殊含义的字符

#以普通字符作为原子(匹配一个普通字符)
'''
strr="花子君八寻宁宁人鱼公主"
pat="花子君"
result=re.search(pat,strr)
print(result)
'''

#匹配通用字符
# \w 匹配任意 字母/数字/下划线
# \W 匹配非任意 字母/数字/下划线(与w相反)
# \d 匹配十进制数字
# \D 匹配十进制数以外的内容
# \s 匹配空白字符
# \S 匹配非空白字符

'''
b="3231766228971"
# 匹配1后面有10个数字的字符
# 取消转义以防万一
pat=r"1\d\d\d\d\d\d\d\d\d"
print(re.search(pat,b)) 
'''

# 匹配数字/英文/中文 (通用字符)
# 数字[0-9]
# 英文[a-z][A-Z]
# 中文[\u4e00-\u9fa5] 汉字的字符集 unicode编码 一---龥 中文笔画最多的文字

'''
strr="花子君@@#@#寻sas宁^&宁qwqw322人32公$$主"
#匹配中文 []是一个原子
pat1=r"[\u4e00-\u9fa5][\u4e00-\u9fa5]"
#匹配英文
pat2="[a-z][a-z]"
#匹配数字
pat3="[0-9][0-9]"

result=re.search(pat1,strr)
result2=re.search(pat2,strr)
result3=re.search(pat3,strr)
print(result,result2,result3)
'''

#原子表
#定义一组平等的原子
#每个原子表只能对应一个字符,不能组合
'''
a="lovehyypcthondwdqdwwdeewf"
pat=r"p[yabcd]thon"
print(re.search(pat,a))
'''

#常用元字符 正则表达式中具有特殊含义的字符
# . 匹配任意字符 \n(换行)除外
# ^ 匹配字符串开始位置
# $ 匹配字符串结束位置
# * 匹配重复0次1次多次前面的原子
# + 重复一次或多次前面的原子
'''
d="1501766228915019682928"

pat1="..."
pat2="^135\d\d\d\d"
pat3=".*2928$"

print(re.search(pat3,d))
'''

#匹配固定次数
# {n}前面的原子出现了n次
# {n,}至少出现n次
# {n,m}出现的次数介于n-m之间
'''
d="1501766228915019682928"
pat1=r"\d{4,10}"
print(re.search(pat1,d))
'''

#匹配多个正则表达式 | (或)
'''
a="15017662289"
b="022-1234556"
# 用|连接
pat=r"1[3578]\d{9}|\d{3}-\d{7}"
# pat2=r"\d{3}-\d{7}"

print(re.search(pat,b))
'''

#分组()
'''
a="dbqiudguigiq$!@*python^!(^!@javaigiewq15017662289"

pat=r"@*(.*?)^!" #匹配中间的字符
pat=r"(python.{0,})(java.{0,})(1[5211]\d{9})"
print(re.search(pat,a).group(3))
'''

#贪婪模式和非贪婪模式
#贪婪模式:在整个正则表达式匹配成功的前提下,尽可能多的匹配
#非贪婪模式:在整个正则表达式匹配成功的前提,下尽可能少的匹配(?)
#Python默认的是贪婪模式

'''
strr="花子君<div>寻sas</div>宁^<div>&宁qwqw322人</div>32公$$主"
pat=r"<div>.*</div>" #匹配里面的任意字符

#贪婪模式中 尽可能多的匹配字符 故首个<div>与结尾</div>之间的部分被匹配
print(re.search(pat,strr))

#非贪婪模式 加? 从开头开始匹配,一旦找到就不管后面的呢
pat1=r"<div>.*?</div>"
print(re.search(pat1,strr))
#获取多个
pat1=r"<div>(.*?)</div>"
'''








