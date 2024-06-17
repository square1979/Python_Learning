"""
    pycharm确定这个对象是list类型，自动提示代码
    1.变量的注解 ———— 变量：类型
        元组类型设置类型详细注解，需要将每一个元素都标记出来
        字典类型设置类型详细注解，需要2个类型，第一个是key，第二个是value
    2.在注释中进行类型注解  # type:int
"""
import json
import random

# 基础数据类型的注解
var_1: int = 10
var_2: str = "google"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {'a': 1, 'b': 2, 'c': 3}

# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple1: tuple[int, int, int] = (1, 2, 3)
my_dict1: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}

# 在注释中详细注解
var_10 = random.randint(1, 10)  # type:int
var_20 = json.loads('{"name":"周杰伦"}')  # type:dict[stu, str]


def func1():
    return 10


var_30 = func1()  # type:int
# var_40: int = "going" 不影响程序的对错，仅做提示
