"""
    for 临时变量 in 待处理数据集（序列）：
        循环满足条件应做的事情1
        循环满足条件应做的事情2
        循环满足条件应做的事情3
        for 临时变量 in 待处理数据集（序列）：
            循环满足条件应做的事情1
            循环满足条件应做的事情2
            循环满足条件应做的事情3
"""
i = 0
for i in range(1, 101):
    print(f"今天是向小美表白的第{i}天")
    for j in range(1, 11):
        print(f"送给小美第{j}支玫瑰花")
    print(f"我喜欢你（在第{i}天表白结束）")
print(f"第{i}天，表白成功")
