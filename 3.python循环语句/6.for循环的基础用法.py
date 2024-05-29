"""
    while 循环的循环条件是自定义的，自行控制循环条件
    for循环是一种“轮询”机制，对一批内容进行 “逐个处理“ ———— 遍历循环
    for 临时变量 in 待处理数据集:
        循环满足条件时执行的代码
"""
name = "STARS"
for letter in name:
    # 将name的内容挨个取出赋予letter临时变量
    # 可以在循环体内，对letter进行处理
    print(letter)
