# 任何事物都可以作为变量，而一个变量往往无法用简单的数据结构表示，比如人有姓名年龄身高体重。
# 这些属性视情况而定，有的需要有的不需要，但是一般来讲编程很容易遇到需要很多属性才能实现的功能。
# 因此面向对象一个重要点在于构造合适的对象，对应的结构在python中也就是dict。

# 手动为不同的人一个个写dict有些太复杂了，有很多属性是可以复用、或者大多数dict的某一属性是相同的。
# 为了减少冗余，更好地复用，引入了class的概念，也就是同一类对象，可以通过class来批量生成。

class Dancer(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def dance(self):
        print(self.name, 'is dancing!')

kiki = Dancer('kiki', 18)
kiki.dance() # kiki is dancing!

# 定义在类中的函数统称为方法；
# 上述例子中，__init__是初始化，构建实例时会运行；
# 每个方法第一个参数都是self，指针指向实例本身，是python的固定语法，但是调用方法时不需要传入self（有点呆）；
# 方法的参数都不能有默认值；
# '__'双下划线的前缀表明是个私有变量，python无法强制控制私有变量，实际上可以通过遍历访问到；
# 写成下划线是提醒开发者自己不要擅自访问；

# 下面是继承的例子：
class Gooddancer(Dancer):
    def yell(self):
        print(self.name, 'say: Wow! You can really dance!')
    def age(self):
        print(self.__age)

choochoo = Gooddancer('choochoo', 19)
choochoo.yell() # choochoo say: Wow! You can really dance! # 通过继承获得了Dancer类的__init__方法
# choochoo.age() # 报错AttributeError，私有属性原则上只有类本身能够访问
# 另外，也可以继承多个类，在定义类时依次作为参数传入即可