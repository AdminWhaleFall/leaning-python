#正则表达式
#针对字符串进行数据筛选的表达式 （匹配）

import re

strr="张三李四王五赵柳"

pat="王六" #正则表达式

rst=re.search(pat,strr)

print(rst)




