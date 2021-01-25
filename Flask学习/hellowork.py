'''
Author: whalefall
Date: 2021-01-25 10:50:42
LastEditors: whalefall
LastEditTime: 2021-01-25 13:56:41
Description: 在bilibili学习flask框架
url:https://www.bilibili.com/video/BV1Lf4y117PS?p=7
'''
# 1.从flask模块导入了flask类(类大写开头)
from flask import *

# 2.创建flask对象
# 参数1 __name__,如果从当前文件启动,那么则是__main__,如果是从其他模块调用运行那么则是模块的名字
# 参数2:static_url_path,表示静态资源的访问地址,/static
# 参数3:static_folder,用来存储静态资源的文件夹,默认名称是static
# 参数4:template_folder,模板文件夹,默认值为template

'''加载(load)配置信息 app.config:表示app运行的所有参数信息
1.从配置类对象中加载
    app.config.from_object(obj)
2.从配置文件中加载
    app.config.from_pyfile(file)
3.从环境变量中加载
    app.config.from_envvar(环境变量)
'''
app = Flask(__name__)

# 使用app,通过路由(route)绑定一个视图函数
# tis:视图函数一定要有返回值

# 给路由添加其他的访问方式 get post put delete
# 默认支持GET


@app.route("/", methods=["GET", "POST"])
def hello_world():
    '''
    # 直接返回[响应体,状态码(可以字符串 666),响应头信息(字典)]
    return "hello world Flask",400,{"Content-Type":"application/json","name":"hyy"}
    '''
    '''
    # 使用jsonify,生成json响应体
    dict={
        "name":"hyy",
        "tya":"sas"
    }
    return jsonify(dict)
    # 简化格式
    # return jsonify(name="hyy",tya="asa")
    '''

# 在访问路由的时候指定参数(动态地址)
# @app.route("/<类型:变量名>")
# 类型: int float path(字符串 默认)


@app.route("/<int:age>")
def play_game(age):
    return "the age is %s" % age

# 自定义参数类型(自定义转化器) [选修]

# 重定向:redirect
# 重定向的状态码是302 且是两次请求
# url_for 反解析 返回视图函数所对应的路由地址 url_for("视图函数名",key)


@app.route("/baidu")
def baidu():
    return redirect("http://baidu.com")

# abort&errorhandler 异常处理和捕获
# 访问服务器资源不存在的时候可爆出异常信息 使用errorhandler捕获
# 格式:abort(代号) @app.errorhandler(代号)


@app.route("/error")
def error():
    # 自定义爆出404
    abort(404)

    return "0"

# 只要出现404异常即可,捕捉404错误的视图函数


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return "页面找不到!"

# /XXX/XXX:资源访问  /?name=hyy :查询参数
# request 请求对象参数
# request.data:非表单(ajax)以POST提交的数据
# request.from:表单以POST方式提交的数据
# request.args:获取的是问号后面的查询参数
# request.method:获取的请求方式
# request.url:获取请求的地址
# request.files:获取的是input标签中type类型为file的文件


@app.route("/api/", methods=["GET", "POST"])
def api_test():
    req = request.args  # 返回的是字典
    # print(req["name"]) # 字典不建议用[]取值
    # 一般用字典get方法取值 若获取不到不会报错返回None,且可以设置默认值,更加灵活
    name=req.get("name","hyy")


# if判断是否直接使用当前模块运行程序
if __name__ == "__main__":
    # app.url_map:返回的是app修饰的所以路由和路径之间的映射关系的集合
    # Tis:只有被app.url_map包含进来的地址才可以访问
    print(app.url_map)

    # 运行app程序
    # 参数: host:地址 默认127.0.0.1 port:端口 默认5000 debug:模式 默认Flase
    # debug=Ture 时不需要重启整个程序保存就可重新运行 且如果程序报错了 浏览器/控制台 就可以输出具体错误
    app.run(host="0.0.0.0", port=5000, debug=True)
