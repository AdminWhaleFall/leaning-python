'''
Author: whalefall
Date: 2021-01-25 17:38:17
LastEditors: whalefall
LastEditTime: 2021-01-31 23:00:41
Description: python CSV文件读写学习,好像很有意思的样子,目前已完结 /撒花✿✿ヽ(°▽°)ノ✿
'''
import csv

# 利用DictReader、DictWriter等对该csv文件读写，并输出示例样式的结果.
# "newline="分隔符


# 写入文件 第一种 如果 csvfile 是文件对象，则打开它时应使用 newline=''
with open("test.csv", "w", newline="", encoding="utf8") as csv_file:
    headers = ["username", "age", "addr"]  # 表头
    # 注意数据主体结构
    values = {
        ("张三", 23, "满城"),
        ("李四", 24, "保定"),
        ("王五", 25, "衡水"),
        ("赵六", 26, "邯郸")
    }  # 数据

    writer = csv.writer(csv_file)
    writer.writerow(headers)  # 写入表头
    writer.writerows(values)  # 写入多行数据

# 写入第二种 DictWriter:写入字典
with open("test.csv", "w", newline="", encoding="utf8") as csv_file:
    headers = ["username", "age", "addr"]  # 表头
    values = [
        {"username": "张三", "age": 23, "addr": "保定"},
        {"username": "李四", "age": 23, "addr": "邯郸"},
        {"username": "王五", "age": 23, "addr": "石家庄"},
        {"username": "赵六", "age": 23, "addr": "衡水"},
    ]  # 字典
    writer = csv.DictWriter(csv_file, headers)  # 写入表头
    # 写入表头的时候需要写入writerheader方法
    writer.writeheader()
    writer.writerows(values)


# 读取 第一种:迭代器
with open("test.csv", "r", encoding="utf8") as f:
    reader = csv.reader(f)
    '''
    next() 返回迭代器的下一个项目。
    next() 函数要和生成迭代器的 iter() 函数一起使用。
    '''
    # next(reader) #输出结果会去掉行头标题
    for row in reader:
        print(row)  # 列表
        name = row[0]
        dates = row[-1]
        print({"name": name, "date": dates})

# 用字典方式读取
with open("test.csv", "r", encoding="utf8") as f:
    # 使用DictReader创建的reader是一个迭代器，遍历迭代器返回的数据是一个字典(有序字典)
    # 返回的结果不包含行首的标题
    reader = csv.DictReader(f)
    for row in reader:
        #遍历迭代器返回的数据是一个字典(有序字典)
        print(row) 