"""
    def关键字 可以定义带有名称的函数 def add()
         带有名称的函数，可以基于名称重复使用
    lambda关键字，可以定义匿名函数（无名称）
        无名称的匿名函数，只可临时使用一次
        语法：lambda 传入参数: 函数体(一行代码)
            lambda  是关键字，表示定义匿名函数
            传入参数表示匿名函数的形式参数，如x,y表示接受两个形式参数
            函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码
"""


def test_fun(come):
    result = come(1, 2)
    print(f"结果是：{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
test_fun(lambda x, y: x + y)
test_fun(lambda x, y: x - y)
test_fun(lambda x, y: x * y)
