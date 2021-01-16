import time

def f():
    for x in range(1,11):
        c=yield x
        print("传入的值",c)


c=f()
print(next(c))
print(c.send("nihao"))
print(c.send("nihaohao"))
print(c.send("nihaohao"))
