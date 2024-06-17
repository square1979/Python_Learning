"""
    __init__ 用于创建类对象的时候的初始行为
    __str__ 字符串方法：控制类转换为字符串的方法
    __lt__ 小于符号比较方法
    __le__ 小于等于，大于等于 符号比较方法
    __eq__ 比较运算符实现方法
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ 魔术方法
    # def __str__(self):
    #     return f"Student类对象，name： {self.name}; age: {self.age}"

    # def __lt__(self, other):
    #     return self.age < other.age

    # def __le__(self, other):
    #     return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("任怡旭", 36)
stu2 = Student("周杰伦", 36)
# 不使用魔术方法，print(stu1 == stu2) 比较的是内存地址 ———— 始终不相等
print(stu1 == stu2)
