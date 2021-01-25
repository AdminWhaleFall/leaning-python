'''
Author: whalefall
Date: 2021-01-25 17:38:17
LastEditors: whalefall
LastEditTime: 2021-01-25 20:54:08
Description: python CSV文件读写学习,好像很有意思的样子,以后再咕咕咕叭
'''
import csv

# 利用DictReader、DictWriter等对该csv文件读写，并输出示例样式的结果.
# "newline="就是说因为我们的csv文件的类型，如果不加这个东西，当我们写入东西的时候，就会出现空行
with open("test.csv","w",newline="") as csv_file:
    '''
    delimiter指定用于分隔每个字段的字符，默认值为逗号（,）。
    escapechar指定用于转义分隔符的字符，以防引号未使用。默认值为无转义字符。
    quotechar可选参数指定 writer对象在写入文件时使用哪个字符来引用字段。
    '''
    csv_writer=csv.writer(csv_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # 也可以使用writer对象和 write_row()方法写入 CSV 文件：

     fieldnames = ['emp_name', 'dept', 'birth_month']
     writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
     











