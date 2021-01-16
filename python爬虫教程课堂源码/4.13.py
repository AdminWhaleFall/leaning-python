import re

#match函数和search函数

# match函数--匹配开头
# search函数--匹配任意位置

#这两个函数都是一次匹配，匹配到一次就不再往后继续匹配了

strr="javapythonjavahtmlpythonjs"

pat=re.compile(r"python")

print(pat.search(strr).group())