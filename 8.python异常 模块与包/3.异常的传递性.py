# 异常的传递性：function1中发生异常，异常会传递到function2
# 当function2没有捕捉这个异常，main函数会捕捉这个异常
# 当所有函数都没有捕捉异常的时候，程序就会报错
def func1():
    print("func1开始执行")
    var = 1 / 0
    print("func1执行结束")


def func2():
    print("func2开始执行")
    func1()
    print("fun2结束执行")


def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常信息为：{e}")


main()
