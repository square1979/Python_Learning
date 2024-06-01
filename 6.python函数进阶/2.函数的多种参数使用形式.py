"""
    1.位置参数：调用函数时根据函数定义的参数位置来传递参数
    2.关键字参数：函数调用时通过“键=值”形式传递参数
                可以让函数更加清晰，容易使用，同时也清除了参数的顺序要求
                如果有位置函数，位置函数必须在关键字参数前面，但关键字参数之间不存在先后顺序
    3.缺省参数：缺省参数是指在函数定义中为某些参数提供默认值的一种机制。
              当调用该函数时,如果没有为这些参数提供实际值,则会使用预先设置的默认值
              默认参数必须写到最后面
    4.不定长参数：不确定调用时候会传递多少个参数
                位置传递 :  *args传进参数合并为一个元组tuple
               关键字传递:  **kwargs参数是“键=值”形式，所有的“键=值”都会被kwargs接受，同时组成字典
                            按照 key = value 的形式传递，传进数据组成字典
"""


def uer_info(name, age, gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")


# 位置参数
uer_info("小明", 18, "女")

# 关键字参数
uer_info(name='小王', age=26, gender="男")
uer_info(age=16, name='国王', gender="男")
uer_info("甜甜", age=17, gender="女")


def user_info(name, age, gender='男'):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")


# 缺省参数(默认值)
user_info('Doinb', '26')
user_info('Doinb', '26', "女")


# 不定长定义的形式参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},其内容是：{args}")


user_info(1, 2, 3, '小明', '男孩')


# 不定长——关键字不定长 **args
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},其内容是{kwargs}")


user_info(name='小王', age=11, gender='男')
