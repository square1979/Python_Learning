"""
    1.print语句不换行输出结果：
        print("hello", end="")
        print("world", end="")
    2.制表符
    \t 相当于 Tab，可以让多行字符串进行对齐
        print("hello\t\tWorld")
        print("informed\tBest")
"""
# 定义外层循环的控制变量: 行
i = 1
while i < 10:
    # 定义内层循环的控制变量: 列
    j = 1
    while j <= i:
        print(f"{i}*{j}={i*j} \t", end="")
        j += 1
    print("")
    i += 1
