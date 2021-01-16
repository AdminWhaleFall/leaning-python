# pip install Flask
# 就不折腾什么virtualenv虚拟环境了 能用就行
from flask import *  # 导包
import json

# Flask构造函数使用当前模块（__name __）的名称作为参数。
app = Flask(__name__)


# Flask类的route()函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。
# rule 参数表示与该函数的URL绑定。
# options 是要转发给基础Rule对象的参数列表。
# 出现的是函数test的返回值
# 通过向规则参数添加变量部分<变量>传入函数中 ，可以动态构建URL。
# <int/float/path:变量> 接受的变量 接受用作目录分隔符的斜杠
# /python 或 /python/返回相同的输出
# url一律后面加 / 成为标准url

# url_for()函数对于动态构建特定函数的URL非常有用。该函数接受函数的名称作为第一个参数，以及一个或多个关键字参数，每个参数对应于URL的变量部分。
# User()函数检查接收的参数是否与'admin'匹配。如果匹配，则使用url_for()将应用程序重定向到hello_admin()函数，否则重定向到将接收的参数作为guest参数传递给它的hello_guest()函数。

# 默认情况下，Flask路由响应GET请求 route()装饰器提供方法参数来更改此首选项。

@app.route("/json/<args>/")
def json_test(args):
    # 这是因为json.dumps
    # 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii = False：
    j = ["hyy", "sasa", "asa"]
    j.append(args)
    t = {}
    t["data"] = j
    return json.dumps(t, ensure_ascii=False)


@app.route("/hello/<name1>/")
def admin(name1):
    return "welcome to admin passwd is {}".format(name1)


# url中的变量要与函数中的变量一一对应
@app.route("/user/<name2>/", methods=["GET", "POST"])
def test(name2):
    # 获取get的内容
    if request.method == "GET":
        # 获取指定key的值
        # /user/<name2>/?a=4454
        g = request.args.get("a")
        print(g)
    # 获取post的内容
    elif request.method == "POST":
        p = request.form["a"]
        print(p)


    if name2 == "admin":
        
        print(name2)
        # redirect重定向到另一个函数 可传参数
        return redirect(url_for("admin", name1=str(name2)))
    else:
        # 可以返回 http status
        return "Hello World{}".format(name2), 200


# add_url_rule()函数也可用于将URL与函数绑定
# app.add_url_rule("/", "hello", test)

# 主运行函数
if __name__ == "__main__":
    # 完整运行参数
    # app.run(host, port, debug, options)
    # 调试模式
    # run方法启动Flask应用程序。但是，当应用程序正在开发中时，应该为代码中的每个更改手动重新启动它。为避免这种不便，请启用调试支持。如果代码更改，
    # 服务器将自行重新加载。它还将提供一个有用的调试器来跟踪应用程序中的错误（如果有的话）。
    app.run(debug=True)
