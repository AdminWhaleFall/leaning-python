import xlsxwriter

#创建文件，并添加一个工作表
workbook=xlsxwriter.Workbook('demo.xlsx')
worksheet=workbook.add_worksheet()

#在指定位置写入数据
worksheet.write("A1","我要自学网")
worksheet.write("A2","python初学者教程")

#关闭表格文件
workbook.close()