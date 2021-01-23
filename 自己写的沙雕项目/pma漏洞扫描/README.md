# 宝塔pma漏洞批量扫描

1. 自用，阿里云做了屏蔽。**扫多了会阻止请求**，所以可以使用**http_Proxy.py**获取免费可用代理ip

> 不能用于非法用途，仅供**学习使用**

## 食用方法

- 用nmap扫描网段内的888端口 保存在脚本目录下的pma.txt文件 扫描结果将保存在pmaResult.txt文件

- 扫描多了可能被机房屏蔽ip 可以直接加代理ip

- 需要安装的模块

  ```
  pip install fake_useragent
  pip install requests
  ```

- 用法:
  1.先找到 ip网段 https://blog.csdn.net/nxuu01/article/details/102779652
  2.用nmap扫描该网段开放的888端口保存在pma.txt文件 格式要求：ip:port
  nmap -vv -n --open -p 888 网段 | awk -F'[ /]' '/Discovered open port/{print $NF":"$4}' >> pma.txt