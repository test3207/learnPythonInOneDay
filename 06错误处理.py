# 建议手动写出错误代码后一个个对，这里也有全部的内置错误：
# https://docs.python.org/zh-cn/3/library/exceptions.html
try:
    1/0
except BaseException as e:
    print(e)
else:
    print('no error')
finally:
    print('done')