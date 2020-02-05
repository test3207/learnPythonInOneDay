# 读写文件
with open('./TESTFILE', 'r', encoding = 'utf-8') as f:
    print(f.read())

with open('./TESTFILE', 'w') as f:
    f.write('Hello, world!')

# 读写JSON
import json

# dict与json互转
strValue = json.dumps({'k': 'v'}) # 字符串{"k": "v"}
dictValue = json.loads(strValue) # dict{'k': 'v'}

# python中实例是无法直接转为json的，需要增加中间函数指定转换方式