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


