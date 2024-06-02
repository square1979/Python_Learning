"""
    模块就是一个Python文件，里面有类 函数 变量等
    模块的导入方式：[from 模块名] import [模块|类|变量|函数] [as 别名]
"""
# import 模块名
# # 1.使用import 导入time模块使用sleep功能（函数）
# import time
# print("hello world")
# # 通过【.】可以使用模块内部的全部功能（类、函数、变量）
# time.sleep(5)
# print("like you ")

# # 2.from 模块名 import 功能名
# from time import sleep
# print("开始")
# sleep(3)
# print("结束")

# 3.from 模块名 import * 导入模块的全部功能
# from time import *
# print("开始")
# sleep(3)
# print("结束")

# 4.1 as定义别名 ———— 将time名字用 t 代替
# import time as t
# print("开始")
# t.sleep(2)
# print("结束")

# 4.2 as定义别名 ———— 同理sleep也可以改用 sl调用时sl(5)
from time import sleep as sl
print("开始")
sl(3)
print("结束")
