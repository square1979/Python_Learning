"""
    类的定义和使用： class 类名称:
        class 是关键字，表示要定义类了
        类的属性，即定义在类中的变量（成员变量）
        类的行为，即定义在类中的函数（成员方法）
    创建类对象的语法：
       对象 = 类名称（）
    函数是写到类外面的，方法是类内部的函数 ———— 成员方法
        def 方法名（self,形参1，... ... 形参N）
            方法体
    在方法内部，想要访问类的成员变量，必须使用self
"""


# 定义一个带有成员方法的类
class Student:
    name = None  # 学生姓名

    def say_hello(self):
        print(f"大家好，我是{self.name},希望大家多多关照！")

    def say_hi2(self, msg):
        print(f"大家好！我是{self.name},{msg}")


stu = Student()
stu.name = "贺文"
stu.say_hi2("我错了")

stu2 = Student()
stu2.name = "黄龙"
stu2.say_hi2("不是范家康")
