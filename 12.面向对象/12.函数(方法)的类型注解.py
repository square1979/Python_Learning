"""
    函数(方法)的类型注解 —— 形参注解
    def 函数方法名（形参名：类型, 形参名：类型, ... ...）
        pass
    函数(方法)的类型注解 —— 返回值注解
    def 函数方法名（形参名：类型, 形参名：类型, ... ...） -> 返回值类型：
        pass
"""


# 对形参进行类型注解
def add(x: int, y: int):
    return x + y


add(1, 2)


# 对返回值进行类型注解
def func(data: list) -> list:
    return data
