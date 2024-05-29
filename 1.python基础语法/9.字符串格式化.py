"""
    %s 将内容转换成字符串形式 放入占位位置
    %d 将内容转换成整数形式 放入占位位置,
    %f 将内容转换成浮点形式 放入占位位置
"""
# % 代表站位 s 将变量（或数字）变成字符串放入站位的地方
class_num = 57
avg_salary = 100
message = "python大数据，本科%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)
# 通过占位的形式，完成拼接
name = "long time"
message = "before %s" % name
print(message)
# 通过占位的形式，完成数字和字符串的拼接
age = 23
tall = 1.8
info = "他的年龄是：%s 岁, 身高为：%s m" % (age, tall)
print(info)
# % 代表站位 d 将变量（或数字）变成整数放入站位的地方
phone = "visa"
price = 4699
year = 1.5
message = "手机品牌是：%s 品牌，手机价格是：%d 元，手机使用时间是：%f 年" % (phone, price, year)
print(message)
