# 定义一个函数，可以在定义时为传入的参数指定默认值
def funcA(name='Kiki'):
    print('Wow!', name, 'can realy dance!')

funcA() # Wow! Kiki can realy dance!
funcA('Choochoo') # Wow! Choochoo can realy dance!

# 关于函数部分，入参可以配置得非常详细，考虑了下不算入门场景，暂时写到这里