# 演示python中各种运算符

# 数学运算符号
print("2+2=", 2 + 2)  # 加
print("2-2=", 2 - 2)  # 减
print("2*2=", 2 * 2)  # 乘
print("2/2=", 2 / 2)  # 除 浮点型
print("11 //2=", 11 // 2)  # 整除
print("9%2=", 9 % 2)  # 取余
print("2 ** 2=", 2 ** 2)  # 乘方

# 赋值运算符—— “=”
a = 20
c = 10
c += a  # c = c + a  30
print(c)
d = 20
d -= a  # d = d - a  0
print(d)
e = 30
e *= a  # e = e * a 600
print(e)
f = 40
f /= a  # f = f /a = 40 / 20 = 2.0  直除
print(f)
g = 50
g %= a  # g = g % a = 50 % 20 = 10  取余
print(g)
h = 14
i = 2
h **= i  # h = 14 * 14 = 196 乘方
print(h)
j = 60
j //= a  # j = j // a = 60 // 20 = 3 整除
print(j)
