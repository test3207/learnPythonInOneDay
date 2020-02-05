# 流程控制类
# for in 循环
nums = [1, 2, 3]
for num in nums:
    print(num)
# while 循环
while len(nums) > 0:
    print(nums.pop(0)) # pop是弹出指定位置的元素，默认为从最后开始弹出
# if elif else 判断 continue 继续 break 中断
while len(nums) < 1000:
    if len(nums) == 0:
        nums.append(0)
    elif len(nums) == 1:
        nums.append(1)
        continue
        nums.append(2) # continue直接执行下一个循环，这一行不会运行 # pylint: disable=unreachable
    else:
        break # 终止循环
# 主要关键字都需要加':'冒号，代码块通过缩进来区分，一般采用4个空格作为下一级代码块
# 以及注意python里面没有其他语言类似i++的写法！

# def 定义函数的关键字，在下一个部分讲

# 逻辑运算符 and or not，没有 xor ，以下结果都是True
True and True
False or True
not False

# in not in，以下结果都是True
1 in [1, 2, 3]
0 not in [1, 2, 3]

# 错误处理 try except else finally raise
try:
    1/0
except BaseException as e:
    print(e)
else:
    print('no error')
finally:
    print('done')