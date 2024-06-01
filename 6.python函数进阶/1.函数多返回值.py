"""
    若两个return语句，仅仅执行第一个return语句
    如果函数有多个返回值，要按照返回值的顺序，写对应顺序的多个变量接受即可
    变量之间用逗号隔开
    支持不同类型的数据return
"""


def test_return():
    return 1, 'hello', [1, 2, 3, 4, 5]


x, y, z = test_return()
print(x, y, z)
