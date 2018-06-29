from urllib import request
from urllib import parse


# textPage = request.urlopen("https://fengshenfeilian.github.io/")
# print(str(textPage.read(),'utf-8'))


# headers = {
#     'X-Bmob-Application-Id': "43199c324d3bcb01bacdbd0914277ef0",
#     "X-Bmob-REST-API-Key": "d4ac4f967651b0a0053a9d3c45c3efa8"
# }
# params = dict()
# params['bql'] = 'select count(*) from WIWJHouse'
# url_values = parse.urlencode(params)
# url = "https://api.bmob.cn/1/cloudQuery?"
# req = request.Request(url + url_values, headers=headers)
# response = request.urlopen(req).read()
# print(response.decode('UTF-8'))


class Dog:
    # 注意这个变量值的变化
    bones = list()
    sex = "man"
    # 私有属性
    __sex2 = "hi"

    def __init__(self, name):
        print("构造函数")
        self.name = name

    def __del__(self):
        print("析构函数")

    def bulk(self):
        print("wang wang %s" % self.name)

    # 私有方法
    def __play(self):
        pass


dog = Dog("123")
dog.bulk()
dog.bones.append("from 1")
print(dog.bones)
dog.sex = "女"
print(dog.sex)

dog2 = Dog("456")
dog2.bones.append("from 2")
print(dog2.bones)
print(dog2.sex)


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s 吃饭" % self.name)

    def sleep(self):
        print("%s 睡觉" % self.name)

    def play(self):
        print("%s 打豆豆" % self.name)


class Man(People):
    def play(self):
        # 调用父类的方法
        People.play(self)
        print("%s 不打豆豆" % self.name)


class Woman(People):
    # 重写构造方法
    def __init__(self, name, age, money):
        # 两种super方法
        # People.__init__(self, name, age)
        super(Woman, self).__init__(name, age)
        self.money = money

    def show_money(self):
        print("%s" % self.money)


# 新式写法
class Relation(object):
    def make_friends(self, obj):
        print("%s 与 %s 是好朋友" % (self.name, obj.name))


# 多继承
class OldMan(Relation, People):
    def __init__(self, name, age):
        # 多继承的构造函数只执行第一个的
        super(OldMan, self).__init__(name, age)


# 继承
man = Man("RY", 30)
man.eat()
man.sleep()
man.play()

woman = Woman("PQ", 28, 15000)
woman.show_money()

old1 = OldMan("old1", 30)
old2 = OldMan("old2", 30)
old2.make_friends(old1)
