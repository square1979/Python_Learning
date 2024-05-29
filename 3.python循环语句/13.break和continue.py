"""
    continue 临时中断 ——  中断本次循环，直接进入下一次循环
        for i range(1, 100): ———— 2
            语句1
            if i in range(1, 100): ———— 1
                语句2
                continue
                语句3
            语句4
    语句3不会执行，语句1 语句2 语句4会执行

    break 永久中断循环
    for i in range(1,100):
        语句1
        break
        语句2
    语句3

    仅对当次循环起作用，不对上次循环起作用
"""

# continue 中断当次循环执行
# for i in range(1, 3):
#     print("语句1")
#     for i in range(1, 3):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")

# break 直接结束循环
# for i in range(1, 3):
#     print("语句1")
#     for j in range(1, 999):
#         print("语句2")
#         break
#         print("语句3")
#     print("语句4")
