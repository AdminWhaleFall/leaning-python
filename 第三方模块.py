# 第三方模块路径
# C:\Users\27341\AppData\Local\Programs\Python\Python37-32\Lib\site-packages
# pip安装第三方模块
# 升级pip cmd输入 python -m pip install --upgrade pip
# 国内的pip源有点慢 要换源
# win+R 打开用户目录%HOMEPATH%，在此目录下创建 pip 文件夹，在 pip 目录下创建 pip.ini 文件, 内容如下
# 用的是清华源
'''
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
'''
# 出现Requirement already up-to-date: (要求已更新) 则更新成功！
# 安装第三方模块 pip install pillow
# 列出第三方包 pip list
# 卸载第三方包pip uninstall pillow
# 
# 离线安装第三方模块
# 先下载 .whl 文件 注意Python版本和系统架构
# 在文件管理器按住shift不放 右键打开cmd
# 执行pip install XXX.whl