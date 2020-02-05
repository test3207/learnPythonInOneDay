# 主要分为全局的内建函数和针对某些类型的内建函数及特性
# 全部内置函数在这里可以找到：https://docs.python.org/zh-cn/3/library/functions.html
# 这里只选取其中比较常用的进行说明

# 全局
# 类型转换函数，将入参转变为指定类型（如果可以转变的话）
int()
float()
str()
bool()

list()
tuple()
dict()
set()

# 输出函数
print('123') # 打印123
# 输入函数，阻塞等待用户输入，输入回车键后返回字符串
inputValue = input()

# 返回长度
len([1, 2, 3]) # 3
# 返回绝对值
abs(-1) # 1
# 返回最大值/最小值
max([1, 3, 5]) # 5
min([1, 3, 5]) # 1
# 幂运算
pow(10, 2) # 100
# 求和
sum([1, 2, 3]) # 6

# 返回类型
type(1) # <class 'int'>
# 检查是否实例
isinstance([], list) # True

# 返回属性，包括私有属性
dir({'key': 'value', 'key2': 'value2'})
# 过滤器
def filterFunc(i):
    return i % 2 == 0
list(filter(filterFunc, [1, 2, 3, 4])) # [2, 4]
# 对象唯一标识符（实现为地址）
id(filterFunc)

# 基于数据类型 todo
# 所有基于数据类型的函数都可以直接通过'.'字符查看，也有函数的基本用法
# str


# list


# tuple


# dict


# set
