# 装饰器
import time


def timer(func):
    def deco(*args, **kwargs):
        func(*args, **kwargs)
        print("执行完毕")

    return deco


@timer
def test1():
    print("Hi test1")


test1()


def login(type):
    def outerwrapper(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print("获取到参数："+type)
            for value in args:
                print(value)
            for key, value in kwargs:
                print(value + " " + value)
        return wrapper
    return outerwrapper


@login("internet")
def loginChaeck(name, pwd):
    print("loginChaeck")


loginChaeck("abc", "1234")

# 列表生成式
a = [i * 2 for i in range(10)]
print(a)


def func(i):
    return i * 3


b = [func(i) for i in range(10)]
print(b)

# 生成器 只有在调用的时候才会生成相应的数据
# 只记录当前位置
# 只有一个__next__()方法
c = (func(i) for i in range(10))
print(c)
valueC = c.__next__()
print(valueC)
valueC = c.__next__()
print(valueC)


def fib(max):
    n, aValue, bVable = 0, 0, 1
    # 相当于
    # t = (0, 0, 1)
    # n = t[0]  aValue = t[1]  bVable = t[2]
    while n < max:
        print(bVable)
        aValue, bVable = bVable, aValue + bVable
        n = n + 1


fib(10)


# 变成生成器
def fib1(max):
    n, aValue, bVable = 0, 0, 1
    # 相当于
    # t = (0, 0, 1)
    # n = t[0]  aValue = t[1]  bVable = t[2]
    while n < max:
        yield bVable
        aValue, bVable = bVable, aValue + bVable
        n = n + 1
    # 异常时候使用
    return "---done---"


d = fib1(10)
print(d)
valueD = d.__next__()
print(valueD)
valueD = d.__next__()
print(valueD)

while True:
    try:
        d.__next__()
    except StopIteration as e:
        print(e.value)
        break


def consumer(name):
    print("%s 开始吃包子了" % name)
    while True:
        baozi = yield
        print("包子%s来了，被%s吃了" % (baozi, name))


cs = consumer("PQ")
cs.__next__()
# 可以发送数值并唤起yield所在方法
cs.send("small baozi")

# 使用iter可以将list dist str等Iterable转换成Iterator 迭代器
e = iter({1, 2, 3, 4})
eValue = e.__next__()
print(eValue)

# 内置函数
f = [1, 0, -1]
# 所有元素全部为true即为true
print(all(f))
# 只要一个元素为true即为true
print(any(f))
# 十进制转二进制
print(bin(10))
# 判断元素是否为true
print(bool(1))
print(bool(0))
print(bool(-1))
# 字节数组
b1 = bytes("abcde", encoding="utf-8")
print(b1)
b2 = bytearray("abcde", encoding="utf-8")
b2[0] = 50
print(b2)
# 通过数字返回相对应的ASCII
print(chr(100))
# 通过ASCII返回相对应的数字
print(ord('b'))
# exec执行程序
code = """
for i in range(10):
    print(i)
"""
exec(compile(code, "", "exec"))
code1 = """
1+2/1*6
"""
com = compile(code1, "", "eval")
print(com)
eval(compile(code1, "", "eval"))
# 显示对象有哪些方法可以使用
print(dir([]))
# 将字符串转换成列表、Set、元组、字典
gValue = "[1,2,3,4,5]"
print(type(eval(gValue)))
gValue = "{1,2,3,4,5}"
print(type(eval(gValue)))
gValue = "(1,2,3,4,5)"
print(type(eval(gValue)))
gValue = "{'key1':'value1'}"
print(type(eval(gValue)))
# 匿名函数只能执行简单的三元运算
cal = lambda a, b: a if a > b else b
print(cal(1, 2))
# 过滤
filt = filter(lambda n: n > 5, range(10))
print(filt)
for i in filt:
    print(i)
# 转换
ma = map(lambda n: n * n, range(10))
print(ma)
for i in ma:
    print(i)

# json序列化与反序列化
import json

infoValue = {"key1": "value1", "key2": "value2"}

# f1 = open("day4.txt", "w")
# # f1.write(str(infoValue))
# f1.write(json.dumps(infoValue))
# f1.close()

# f2 = open("day4.txt", "r")
# print(eval(f2.read()))
# print(json.loads(f2.read()))
# f2.close()

# pickle对复杂对象进行序列化与反序列化
import pickle


def pickletest():
    print("Hello")


infoValue2 = {"key1": "value1", "key2": "value2", "func": pickletest}
# f1 = open("day4.txt", "wb")
# # f1.write(pickle.dumps(infoValue2))
# pickle.dump(infoValue2, f1)
# f1.close()

f2 = open("day4.txt", "rb")
# data = pickle.loads(f2.read())
data = pickle.load(f2)
data["func"]()
f2.close()

# 项目路径
import os

print(os.path.dirname(os.path.abspath(__file__)))
