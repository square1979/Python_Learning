"""
    给定一个字符串"itheima itcast boxuegu"
    1.统计字符串内有多少“it”字符
    2.将字符串内的空格，全部替换为字符：“|”
    3.并按照“|”进行字符串分割,得到列表
"""
str1 = 'itheima itcast boxuegu'
num1 = str1.count("it")
print(f"字符串{str1}中有：{num1}个it字符")
str2 = str1.replace(" ", "|")
print(f"字符串{str1},被替换空格后，结果为：{str2}")
list1 = str2.split("|")
print(f"字符串{str2},按照|分隔后，得到：{list1}")
