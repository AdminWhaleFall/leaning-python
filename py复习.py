# 变量 Number 类型
# 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
a = 2
print(type(a))
# 浮点型(float) 小数
b = 2.21
print(type(b))
# 字符串 (str)
c = "宁宁喜欢花子丫"
print(type(c))
# 字符串拼接与切片 [第一个算:第二个不计入] 索引从0开始
print("谁",c[0:2],"喜欢",c[4:6],"合起来:",c[:6])

#各种容器
#列表 [元素,元素,元素]
list1 = ["颖怡","飞扬","喜欢",17,1,2020]
list2 = [1,2,3,4,"颖怡","丹羽",17]
list3 = ["a","b","c"]
list4 = [1,2,432,3131,313]
# 通过索引访问列表的值 支持切片 [-4,-1]取倒数第4个到倒数第一个
print(list1[1],list1[2],list2[4:6],list2[-4:-1])
# 更新列表
list1.append("徐楚莹") #添加
# print(list1)
del list1[0] #删除
# print(list1)
# 或者直接给列表中的数据赋值
list1[0] = "不喜欢"
print(list1)
# 一些方法
# 必须纯数字！
print("列表元素最大值 =",max(list4))
print("列表元素最小值 =",min(list4))
print("列表元素个数 =",len(list4))
# 查找
print("颖怡" in list1)
# 转化为元组
l2t = tuple(list1)
print(type(l2t))

#元组(tup) (与列表类似 但是不能修改！)
tup1 = ("鲸落","phsics",1,234,133)
tup2 = ("21",) #元组中只包含一个元素时，需要在元素后面添加逗号
# 与列表一样的取法 支持切片
print(tup1[0])
#tup1[0] = "修改元组" 元组不能被修改！
#查找
print(3 in tup1)
# 转化为列表 用一个东西接收
t2l = list(tup1)
print(type(t2l))

# 字典(键对值) 键是惟一的,重复则替换 注意:值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dic = {2:12,"hobby":"追番","key":"value"}
print(dic[2])
# 修改
dic["hobby"] = "谈恋爱"
print(dic["hobby"])
dic["喜欢的人"] = "hyy" #添加
print(dic["喜欢的人"])
print("字典个数:",len(dic))
print(type(dic))
print(str(dic))
del dic["喜欢的人"]  # 删除键
dic.clear()      # 清空字典所有条目
del dic          # 删除字典

#集合(set)
set() #创建空集合
set = {"wow","wqw","hyy"}

