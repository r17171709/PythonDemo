import datetime
import time
import random
import os

time.time()
# time.sleep(1)
print(time.localtime())
print(time.localtime().tm_year)
print(time.mktime(time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strptime("2018-06-22 09:40:54", "%Y-%m-%d %H:%M:%S"))

# 当前时间
print(datetime.datetime.now())
# 当前时间往后退3天后的时间
print(datetime.datetime.now() + datetime.timedelta(3))

print(random.randint(1, 3))
# 随机从字符串中取1个值
print(random.choice("abcd"))
# 随机取2个值
print(random.sample("abcd", 2))
# 随机打乱
a = [1, 2, 3, 4]
random.shuffle(a)
print(a)

# 随机数验证码
random_value = ""
for i in range(0, 4):
    if i == random.randrange(0, 4):
        current = chr(random.randrange(65, 90))
    else:
        current = random.randint(0, 9)
    random_value = random_value + str(current)
print(random_value)

# 获取当前工作目录
print(os.getcwd())
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.getcwd())
# 改变当前工作目录
os.chdir("C:\\")
print(os.getcwd())
# 省去转义
os.chdir(r"D:\workspace")
print(os.getcwd())
# 当前目录
print(os.curdir)
# 创建文件夹
os.makedirs(r"C:\a\b")
# 清理空文件夹
os.removedirs(r"C:\a\b")
# 创建单级目录
os.mkdir(r"c:\a")
# 删除单级空目录
os.rmdir(r"c:\a")
# 列出制定目录下的所有文件和子目录
print(os.listdir(r"."))
# os.remove()
# os.rename()
os.path.exists(r"c:")
