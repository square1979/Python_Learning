# 传入计算逻辑，而非传入数据
def test_fun(nike):
    result = nike(1, 2, 3)
    print(f"参数的类型是：{type(nike)}")
    print(f"计算结果：{result}")
    return result


def com(a, b, c):
    return a + b + c


test_fun(com)
