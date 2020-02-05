# 考虑到语义连贯性，部分排版、代码格式没有做到最佳实践，不影响使用，但是建议后续自行开发前阅读pep8规范：
# https://www.python.org/dev/peps/pep-0008/

# 注释呢就是如你所见#号开头的，没有多行注释，你得手动一行行注释

# 任何事物都可以是变量。在python中没有声明变量这个概念，赋值即定义
idValue = 'test3207'
# 上述变量名为idValue，值为字符串test3207。变量名是唯一的。命名规则太长懒得讲，就别花里胡哨，老老实实用英文开头

# 下面是基本数据类型
intValue = 1 # 整数
floatValue = 1.23 # 浮点数
strValue = '1.23' # 字符串
boolValue = True # bool
noneValue = None # 空值

# 下面是复杂数据类型，或者别的什么叫法。除了基本数据类型的都是复杂数据类型，两者的区别在哪里？
# 基本数据类型的赋值都是原始的：原始在完全开辟了一片内存空间；而复杂数据类型是复用的；
# 例如：
intValue2 = intValue
print(intValue, intValue2) # 1 1

# 这一例中，内存里就同时存在两个值为1的区块，而且是互不影响的
intValue2 = 2
print(intValue, intValue2) # 1 2

# 而复杂数据类型如果直接通过变量赋值，本质上传递的是内存地址，也就是会互相影响的：
listValue = [] # 有序数组
listValue2 = listValue
print(listValue, listValue2) # [] []
listValue2.append(1) # append函数是给有序数组插入元素，函数后续再讲解，这里只需要了解意思
print(listValue, listValue2) # [1] [1]
# 以上就是基本和复杂的区别

# list还有一个哥哥叫tuple，唯一的区别就是list的元素可变，tuple的元素不可变
listValue2[0] = 666
print(listValue2) # [666]
tupleValue = (1, 2, ['a'])
# tupleValue[0] = 666 # 会报错TypeError

# 然而下面这行又可以运行
tupleValue[2].append('b')
print(tupleValue) # (1, 2, ['a', 'b'])
# 原因和上面讲的list赋值一样，tupleValue[2]存的是['a']所在的内存地址，而非这个数组本身；修改数据并不会改掉这个地址
# 注意，以上的简单复杂、传内存地址在很多语言中都是通用的

# 复杂数据类型还有dict和set
# dict是面向对象中很重要的部分，便于描述对象，下面的name、age都是属性，'test3207'、18则是对应的属性值，每个dict的每个属性都是唯一的
dictValue = {
    'name': 'test3207',
    'age': 18
}
# set往后用得到再说，主要用于去重
setValue = {1, 2, 3}
