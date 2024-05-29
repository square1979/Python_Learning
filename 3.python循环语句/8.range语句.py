"""
    1.range(0,num) ———— 从零开始到num结束的数字序列怕【不含num】
    2.range(num1,num2) ———— 从num1开始到num2结束的数字序列【不含num2本身】
    3.range(num1,num2,step) ———— 从num1开始到num2结束，数字之间的步长以step为准的序列【不含num2本身】
"""
for i in range(10):
    print(f"i = {i}\t", end="")
print()
for j in range(5, 10):
    print(f"j = {j}\t", end="")
print()
for k in range(5, 10, 2):
    print(f"k = {k}\t", end="")
print()
for x in range(5):
    print("送玫瑰花\t", end="")
