import flask

a = [312, 31344, 324, 314, 423, "b", 431, 0, 3, 42134]

# for循环遍历列表
for i in a:
    print("-------", i)
    # print(3/i) 狂报错
# try...except 输出错误详情 但不终止程序运行丫
    # 内置异常
    try:  # 写可能会报错或出现异常的代码
        print(3/i)
    # 捕获try语句里边的异常 Exception就是捕获异常的对象
    except Exception as e:
        # 如果出现异常则运行下面的语句
        print("出现错误:", e)
    else:
        # 没有异常则运行下面语句
        print("运行正常鸭")
    finally:
        # 无论是否有异常都会执行的语句 比如关闭文件资源
        print("本次结束")

# 抛出自定义异常
pwd = "123456"
if len(pwd) < 8:
    # 实例化Exception类 传入自定义错误信息
    # 语句中Exception是异常的类型（例如ValueError），参数是一个异常参数值。
    ex = Exception("密码不能低于8位数")
    # print("密码不能低于8位数")
    raise ex  # 抛出自定义异常 直接让程序报错
else:
    print("密码设置成功11")

