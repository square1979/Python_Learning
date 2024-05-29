# 局部变量：定义在函数体内部的变量，只在函数体内生效，完成后销毁变量
# print(num)×
def testa():
    num1 = 100
    print(num1)


testa()

# 全局变量:在函数体内，体外都能生效的变量
num = 200


def test_b():
    print(f"test is {num} ———— b")


def test_c():
    global num  # 关键字声明 num 是全局变量
    num = 500
    print(f"test_c is {num} ———— c")


test_b()
test_c()
print(num)
