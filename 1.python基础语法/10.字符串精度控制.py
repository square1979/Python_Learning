"""
    使用辅助符号 “m.n" 控制数据的宽度和精度
    m 控制宽度 要求是数字 设置宽度小于数字自身不生效
    .n 控制小数点精度，要求是数字，会进行小数的四舍五入
"""
num1 = 11
num2 = 22.3369
print("数字11 限制宽度为5，结果是：%5d" % num1)
print("数字11 限制宽度为1，结果是：%1d" % num1)
print("数字22.3369 宽度限制7，小数精度2.结果是：%7.2f" % num2)
print("数字22.3369 宽度不限制，小数精度2.结果是：%.2f" % num2)
