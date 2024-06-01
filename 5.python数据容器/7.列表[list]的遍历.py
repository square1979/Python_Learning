"""
    利用while循环列表:利用列表[下标]的方式取出,从零开始,每次加1 的控制循环条件
    index = 0
    while index<len(data):
        元素 = data[index]
        对元素进行处理
        index += 1

    利用for循环列表: 利用列表[下标]的方式取出
    for 临时变量 in data:
        对临时变量进行处理

    区别：1.循环控制上：
        while可以自定义循环条件 可自行控制
        for不可以自定循环条件 只可以一个个从容器内取出数据
         2.在无无限循环上：
        while循环可以通过条件控制做到无限循环
        for循环理论上不可以
         3.使用场景上：
        while循环适用于任何想要循环的场景
        for循环适用于遍历数据容器或者简单的固定次数循环的场景
"""


# while循环输出列表元素
def list_while(data):
    index = 0
    while index < len(data):
        print(data[index])
        index += 1


data_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_while(data_1)


# for循环对列表遍历
def list_for(data):
    for index in data:
        print(index)


data_2 = ['a', 'b', 'c', 'd', 'e', 'f']
list_for(data_2)
