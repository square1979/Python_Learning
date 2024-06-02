# __ all__ 变量的功能：如果模块文件中有"__all__"变量
# 当使用from 模块名 import * 导入时，只能导入这个列表中的元素
# 列表控制能被调用的函数

__all__ = ['function_A']


def function_A(a, b, c):
    print(a + b + c)


def function_B(a, b, c):
    print(c - b + a)


if __name__ == '__main__':
    function_A(1, 2, 3)
