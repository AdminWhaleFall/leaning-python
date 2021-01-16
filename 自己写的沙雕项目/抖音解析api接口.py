from flask import Flask,request
import json
 
app=Flask(__name__)
 
# 只接受get方法访问
@app.route("/dy",methods=["GET"])
def check():
    # 默认返回内容
    return_dict= {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    print(dict(request.args))

    if dict(request.args)=={}:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data=request.args.to_dict()
    name=get_data.get('name')
    age=get_data.get('age')
    # 对参数进行操作
    return_dict['result']=tt(name,age)
    
    # 这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：
    return json.dumps(return_dict, ensure_ascii=False)
 
# 功能函数
def tt(name,age):
    result_str=name+"今年"+age+"岁" 
    return result_str
 

app.run(host='0.0.0.0',port=8888)