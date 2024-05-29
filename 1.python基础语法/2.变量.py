# 在程序运行时，能储存计算结果或能表示值的抽象概念
# 格式：变量名 = 变量值
money = 50
print("当前钱包余额：", money, "元")
# 买了冰激凌花费十元
ice = 10
print("购买了冰激淋，花费：", ice, "元")
coke = 5
print("购买了可乐，花费：", coke, "元")
money = money - ice - coke
print("最终，钱包里剩余：", money, "元")
