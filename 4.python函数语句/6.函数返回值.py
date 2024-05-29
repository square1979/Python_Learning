# 函数执行后，将结果返回给调用者； 写在return后的代码不会执行
def add(a, b):
    return a + b


r = add(1, 2)
print(r)
