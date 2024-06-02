"""
    1.新建一个Python文件，命名为my_module1.py 并定义test函数
    2.如果导入多个模块且模块内有同名功能，当调用同名功能时，调用到的是后面导入的模块的功能
    3.模块内有输出，导入后自动输出数值
"""
# import my_module1
# my_module1.function_A(1, 2, 3)

# from my_module1 import function_A
# from my_module2 import function_A
# function_A(1, 2, 3)

# __main__变量的功能,不执行调用模块的内部输出
# 使用【from my_module1 import *】导入模块，只导入了function_A
from my_package.my_module1 import *

function_A(1, 2, 3)
# function_B(1,2,3)
