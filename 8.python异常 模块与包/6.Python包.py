"""
    1.python包就是一个文件夹；文件夹中存有多个模块+【_init_.py】文件 = package 包
    2.__init__.py 文件是默认Python软件包默认创建的文件，通过这个文件来表示文件夹是Python的包
    3.__all__ 变量的作用：通过 __all__ = ["module1","module2","module3"]控制import导入内容
"""
# 创建一个包
# 1.导入自定义的包中的模块，并使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print()
# my_package.my_module2.info_print2()

# 2.导入自定义的包中的模块，并使用
# from my_package import my_module1
# from my_package import my_module2
#
# my_module1.info_print()
# my_module2.info_print2()

# 3.导入函数功能
# from my_package.my_module1 import info_print
# from my_package.my_module2 import info_print2
#
# info_print()
# info_print2()

# 通过__all__ 变量，控制import *
from my_package import *

my_module1.info_print()
# my_module2.info_print2()
