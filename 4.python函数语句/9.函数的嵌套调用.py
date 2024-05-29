# 在一个函数里面又调用了另一个函数
# 函数a中执行到调用b的语句，会将函数b全部执行完成后，继续执行函数a的剩余内容

# 定义funB
def fun_b():
    print("-- 2 --")


# 定义funA
def fun_a():
    print("-- 1 --")

    # 嵌套调用funB
    fun_b()

    print("-- 3 --")


# 调用函数funA
fun_a()
