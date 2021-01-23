'''
Author: whalefall
Date: 2021-01-22 21:48:48
LastEditors: whalefall
LastEditTime: 2021-01-23 10:33:05
Description: python数据可视化绘图(学习向)
url:https://blog.csdn.net/qq_34859482/article/details/80617391
'''


import matplotlib.pyplot as plt  # plt绘图
# 在任何绘图之前，我们需要一个Figure对象，可以理解成我们需要一张画板才能开始绘图。
fig = plt.figure()
# 在拥有Figure对象之后，在作画前我们还需要轴，没有轴的话就没有绘图基准，所以需要添加Axes。也可以理解成为真正可以作画的纸。
# 参数的解释的在画板的第1行第1列的第一个位置生成一个Axes对象来准备作画
# 生成Axes，前面两个参数确定了面板的划分，例如 2， 2会将整个面板划分成 2 * 2 的方格，第三个参数取值范围是 [1, 2*2] 表示第几个Axes。如下面的例子：
''' 添加一个画纸
ax = fig.add_subplot(1,1,1)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',ylabel='Y-Axis', xlabel='X-Axis')
plt.show()
'''

# fig 还是我们熟悉的画板， axes 成了我们常用二维数组的形式访问，这在循环绘图时，额外好用。
'''也可添加多个画纸
# row:行数 cols:列数
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0,0].set(title='Upper Left')
axes[0,1].set(title='Upper Right')
axes[1,0].set(title='Lower Left')
axes[1,1].set(title='Lower Right')
'''

# 适用于简单快速画图(折线)
'''
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.xlim(0.5, 4.5)
plt.show()
'''

# 基本绘图2D
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)

# 设置图例,表头
# ylabel:y坐标标签 xlabel:坐标标签 title:表头
ax1.set(ylabel='Temperature (deg C)',
        xlabel='Time', title='A tale of two cities')
# 显示图例说明 可以传入图例显示的位置
ax1.legend("best")
# 1.线
# plot()函数画出一系列的点，并且用线将它们连接起来。看下例子：
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 2, 3, 4, 5, 6]
# marker:记号标志 linestyle:线的风格 linewidth:线的宽度 markersize:记号笔大小 'go--':MATLAB风格 label:图例
ax1.plot(x, y, color='red', marker='2',
         linestyle='dashed', linewidth=2, markersize=12, label="test")
# plt.show() # 画完所有再show

# scatter():散点图 不画线只画点
ax2.scatter(x, y, color='red', marker='+')

# 条形图 打横:bar() 打竖:barh()  align:对齐方式
x3 = ["a", "b", "c"]
y3 = [1, 3, 6]
r = ax3.bar(x3, y3, color="lightblue", align="center")  # 返回的是一个迭代器
# axvline:在垂直方向上划线 axhline:在水平方向上划线
ax3.axhline(5, color="gray", linewidth=2)
print(r)

'''以前使用迭代器的方法 (舍弃)
# for i in r:
#     print(i)
'''

'''现在使用zip()方法
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表 一一对应
#>>[(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
#>>[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
'''

# 接受ax3.bar的bar对象以便修改 y3是源数列
for bar, height in zip(r, y3):
    if height > 5:
        # edgecolor:边色
        bar.set(edgecolor='darkred', color='salmon', linewidth=0.8)

plt.show()

# 3 布局、图例说明、边界
'''
ax.set_xlim([xmin, xmax])   #设置X轴的区间
ax.set_ylim([ymin, ymax])   #Y轴区间
ax.axis([xmin, xmax, ymin, ymax])   #X、Y轴区间

ax.set_ylim(bottom=-10)     #Y轴下限
ax.set_xlim(right=25)       #X轴上限
'''
