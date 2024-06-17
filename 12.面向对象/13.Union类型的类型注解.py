"""
    使用union[类型， ... ，类型] 可以定义联合类型注解
"""
# 使用union类型必须先导入包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, 3, 'google', 'mark']


def func(data: Union[int, str]) -> Union[int, str]:
    return data


func("happy")
